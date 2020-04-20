import datetime

from django.db import models
from django.utils import timezone

class Item(models.Model):
    price = models.DecimalField('ціна', max_digits = 6, decimal_places = 2)
    is_in_stock = models.BooleanField('наявність', default = True)
    artist = models.ForeignKey('виконавець', max_length = 30)
    album = models.ForeignKey('альбом', max_length = 30)
    genre = models.ForeignKey('жанр', max_length = 20)   
    image = models.ForeignKey(upload_to='item_images/')
    discount = models.IntegerField('знижка', default = 0)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return %s %s %(self.artist, self.album)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товари'

