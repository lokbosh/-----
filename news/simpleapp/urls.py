from django.urls import path
from .views import NewsList,NewsDetail,create_post,NewsUpdate,NewsDelete
urlpatterns = [
    path('',NewsList.as_view(),name='post_list'),
    path('<int:pk>', NewsDetail.as_view(),name='post_detail'),
    path('create/',create_post,name='post_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]
