from django.db import models

class Client(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)

    def __str__(self):
        return "Клієнт %s" % (self.name, self.surname)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'