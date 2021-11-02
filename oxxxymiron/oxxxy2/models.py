from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse


class News(models.Model):
	text = models.TextField(verbose_name = 'Текст новсти', blank = True)
	title_news = models.CharField(verbose_name = 'Заголовок новости', max_length = 55)
	pub_date = models.DateTimeField(verbose_name = 'Дата публткации')
	photo = models.ImageField(verbose_name = 'Картинка', upload_to = 'photos/', blank = True)
	slug = models.SlugField(verbose_name = 'URL', max_length = 255, unique = True, db_index = True)

	def __str__(self):
		return self.title_news

	def get_absolute_url(self):
		return reverse('detail_news', kwargs = {'news_slug': self.slug})

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'



class Album(models.Model):
	title_album = models.CharField(verbose_name = 'Заголовок альбома', max_length = 55)
	description_album = models.TextField(verbose_name = 'Описание альбома')
	slug = models.SlugField(verbose_name = 'URL', max_length = 255, unique = True, db_index = True)

	def __str__(self):
		return self.title_album


	def get_absolute_url(self):
		return reverse('detail_albums', kwargs = {'album_slug': self.slug})


	class Meta:
		verbose_name = 'Альбом'
		verbose_name_plural = 'Альбомы'

class Trak_in_album(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	author = models.CharField(verbose_name = 'Имена авторов', max_length = 100)
	name_trak1 = models.CharField(verbose_name = 'Название трека', max_length = 20)
	audio = models.FileField(upload_to = 'audio/', blank = True)
	slug = models.SlugField(verbose_name = 'URL', max_length = 255, unique = True, db_index = True)

	def __str__(self):
		return self.name_trak1


	def get_absolute_url(self):
		return reverse('name_trak1', kwargs = {'trak_in_album_slug': self.slug})


	class Meta:
		verbose_name = 'Трек в альбоме'
		verbose_name_plural = 'Треки в альбоме'

class Trak(models.Model):
	author = models.CharField(verbose_name = 'Имена авторов', max_length = 100)
	name_trak = models.CharField(verbose_name = 'Название трека', max_length = 20)
	audio = models.FileField(verbose_name = 'аудио', upload_to = 'audio/', blank = True)
	slug = models.SlugField(verbose_name = 'URL', max_length = 255, unique = True, db_index = True)

	def __str__(self):
		return self.author


	def get_absolute_url(self):
		return reverse('trak', kwargs = {'trak_slug': self.slug})


	class Meta:
		verbose_name = 'Трек'
		verbose_name_plural = 'Треки'

