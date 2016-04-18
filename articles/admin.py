from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info about article', {'fields': [
         'title', 'image', 'text']}),
        ('Author post', {'fields': [
            'author']}),

        ('Public article', {
         'fields': ['is_published']})
    ]
    list_filter = ['author']
    list_display = ('title', 'author',
                    'is_published')
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
