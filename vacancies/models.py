from django.db import models

# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=100, default='S')
    description = models.TextField(default='')
    experience = models.CharField(max_length=100, default='')
    schedule = models.CharField(max_length=100, default='')
    salary = models.CharField(max_length=100, default='')
    email = models.EmailField(default='polotov.arlen@gmail.com', max_length=100)
    whatsapp = models.CharField(max_length=100, default="https://wa.me/996703372542")
    telegram =  models.CharField(max_length=100, default="https://t.me/huriskop")
    Megacom = models.CharField(max_length=100, default="+(996) 555 881 353")
    Oshka = models.CharField(max_length=100, default="+(996) 755 881 353")

    def __str__(self):
         return self.name



