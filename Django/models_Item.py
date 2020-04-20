import datetime

from django.db import models
from django.utils import timezone

class ItemCategory(models.Model):
    category_name = models.CharField('назва категорії'max_length = 30, null = True, blank = True) = models.CharField('arName', max_length = 200)
    is_active = models.BooleanField('активність'default = True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'категорія'
        verbose_name_plural = 'категорії'

class Item(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete = models.CASCADE)
    item_name = models.CharField('назва', max_length = 50)
    is_active = models.BooleanField('активність', default = True)
    price = models.DecimalField('ціна', max_digits = 6, decimal_places = 2)
    description = models.TextField('comment', max_length = 300, blank = True, null = True, default = None)
    discount = models.IntegerField('знижка', default = 0)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товари'

class ItemImage(models.Model):
    item = models.ForeignKey(Item, blank = True, null = True, default = None, on_delete = models.CASCADE)
    image = models.ImageField('фото', upload_to='item_images/')
    is_active = models.BooleanField('активність', default = True)
    is_main = models.BooleanField('головна', default = False)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
 
    def __str__(self):
        return self.id
