from django.contrib import admin
from .models import Terapias, Tags

# Register your models here.

class TerapiasAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'subtitle')
    ordering = ['title']

admin.site.register(Terapias, TerapiasAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ['title']

admin.site.register(Tags, TagsAdmin)