from django.contrib import admin
from blog.models import Category, Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'category', 'publish_date']
    list_display = ('title', 'author', 'publish_date')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
