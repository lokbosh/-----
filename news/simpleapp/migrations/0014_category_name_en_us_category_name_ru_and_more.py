# Generated by Django 4.2.4 on 2023-11-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0013_alter_category_name_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(help_text='Имя категории', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='Имя категории', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='name_en_us',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Имя категории', max_length=100),
        ),
    ]
