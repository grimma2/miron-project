from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
	list_display = ('slug', 'title', 'photo', 'pub_date')
	list_display_links = ('slug', 'title')
	search_fields = ('title', 'text')
	prepopulated_fields = {'slug': ('title',)}


class AlbumAdmin(admin.ModelAdmin):
	list_display = ('slug', 'title', 'description', 'pub_date', 'photo')
	list_display_links = ('slug', 'title')
	search_fields = ('title',)
	prepopulated_fields = {'slug': ('title',)}


class TrakAdmin(admin.ModelAdmin):
	list_display = ('slug', 'name', 'audio', 'photo', 'album')
	list_display_links = ('slug', 'name')
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Trak, TrakAdmin)
