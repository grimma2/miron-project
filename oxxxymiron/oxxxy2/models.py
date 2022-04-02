from django.db import models
from django.urls import reverse


class News(models.Model):
    text = models.TextField('Текст новсти', blank=True)
    title = models.CharField('Заголовок новости', max_length=55)
    pub_date = models.DateTimeField('Дата публткации')
    photo = models.ImageField('Картинка', upload_to='photos_news/', blank=True)
    slug = models.SlugField('URL', max_length=999, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_news', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Album(models.Model):
    title = models.CharField('Заголовок альбома', max_length=55)
    description = models.TextField('Описание альбома')
    photo = models.ImageField('Картинка', upload_to='photos_album/', blank=True)
    pub_date = models.DateTimeField('Дата публткации', auto_now=True)
    slug = models.SlugField('URL', max_length=999, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_album', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Trak(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='trak_set', blank=True, null=True
    )
    name = models.CharField('Название трека', max_length=20)
    audio = models.FileField('аудио', upload_to='audio/', blank=True)
    photo = models.ImageField('Картинка', upload_to='photos_news/', blank=True)
    slug = models.SlugField('URL', max_length=999, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_trak', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
