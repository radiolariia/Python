import datetime

from django.db import models
from django.utils import timezone

class Characteristics(models.Model):
	description = models.TextField('опис',)
	label = models.CharField('Лейбл', max_length = 20, null = True, blank = True)
	release_date = models.DateTimeField('реліз')
	quantity_of_carriers = models.CharField('кількість носіїв', max_length = 10, null = True, blank = True )
	tracklist = tinymce_models.HTMLField(max_length = 5000, null = True, blank = True)
	details = models.CharField('деталі', max_length = 50, null = True, blank = True)
	cd_or_vinyl =
	barcode = models.CharField('штрих-код', max_length = 20, null = True, blank = True) 

	created = models.DateTimeField(auto now add = True, auto now = False)
	updated = models.DateTimeField(auto now add = False, auto now = True)

	def __str__(self):
        return %s %s %(self.artist, self.album)

    class Meta:
        verbose_name = 'опис'

class Record(models.Model):
    artist = models.CharField('виконавець',max_length = 30, null = True, blank = True)
    album = models.CharField('альбом', max_length = 30, null = True, blank = True)
    genre = models.CharField('жанр', max_length = 20, null = True, blank = True)   
    image = models.ImageField(upload_to = 'item_images/', null = True, blank = True, default = "item_images/empty item_image.jpg")    
    link_for_video = models.CharField(max_length = 256, blank = True, null = True, default = None)
    link_for_audio = models.CharField(max_length = 256, blank = True, null = True, default = None)
    characteristics = models.ForeignKey(Characteristics)

    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return %s %s %(self.artist, self.album)

    class Meta:
        verbose_name = 'запис'
        verbose_name_plural = 'записи'