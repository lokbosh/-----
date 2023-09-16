from django.contrib import admin
from .models import Comment,Post,PostCategory,Author,Category

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Category)
