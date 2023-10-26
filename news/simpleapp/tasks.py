from celery import shared_task
import datetime

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news import settings
from .models import Post, Category


@shared_task
def post_created(id):
    instance = Post.objects.get(id=id)

    subscribers_emails = []

    for category in instance.postCategory.all():
        subscribers_emails += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)

    subject = f'Новый пост в категории {instance.postCategory}'

    text_content = (
        f'Название: {instance.title}\n'
        f'Текст: {instance.text}\n\n'
        f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )

    html_content = (
        f'Название: {instance.title}<br>'
        f'Текст: {instance.text}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )

    
    msg = EmailMultiAlternatives(subject, text_content, None, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@shared_task
def weekly_send_emails():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscriptions = set(
        Category.objects.filter(name__in=categories).values_list('subscriptions__user__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscriptions
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()