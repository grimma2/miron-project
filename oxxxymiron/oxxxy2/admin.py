from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
	list_display = ('slug', 'title_news', 'photo', 'pub_date')
	list_display_links = ('slug', 'title_news')
	search_fields = ('title_news', 'text')
	prepopulated_fields = {'slug': ('title_news',)}

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('slug', 'title_album', 'description_album')
	list_display_links = ('slug', 'title_album')
	search_fields = ('title_album',)
	prepopulated_fields = {'slug': ('title_album',)}

class Trak_in_albumAdmin(admin.ModelAdmin):
	list_display = ('slug', 'author', 'name_trak1', 'audio')
	list_display_links = ('slug', 'name_trak1')
	search_fields = ('name_trak1',)
	prepopulated_fields = {'slug': ('name_trak1',)}

class TrakAdmin(admin.ModelAdmin):
	list_display = ('slug', 'author', 'name_trak', 'audio')
	list_display_links = ('slug', 'name_trak')
	search_fields = ('name_trak',)
	prepopulated_fields = {'slug': ('name_trak',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Trak, TrakAdmin)
admin.site.register(Trak_in_album, Trak_in_albumAdmin)
