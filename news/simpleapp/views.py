from typing import Any
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    
    
    
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class NewsUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = ('simpleapp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class NewsDelete(PermissionRequiredMixin,DeleteView):
    permission_required = ('simpleapp.delete_posts',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')