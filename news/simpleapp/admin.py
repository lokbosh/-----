from django.contrib import admin
from .models import Comment,Post,PostCategory,Author,Category

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title','author','dateCreation','categoryType')
    list_filter = ('author', 'dateCreation','title','categoryType')
    search_fields = ('title', 'postCategory__name')# генерируем список имён всех полей для более красивого отображения

admin.site.register(Comment)
admin.site.register(Post,PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Category)
