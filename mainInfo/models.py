from django.db import models

class PopularTeachers(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField(default='No data')
    email = models.EmailField(default='', max_length=100)
    whatsapp = models.CharField(max_length=100, default="Введите ссылку")
    telegram = models.CharField(max_length=100, default="Введите ссылку")
    instagram = models.CharField(max_length=100, default="Введите ссылку")
    def __str__(self):
         return self.name


class AboutInai(models.Model):
    description = models.TextField(default='Inai twe')
    image = models.ImageField(default='i')
    quote = models.TextField(default='Start something that matters')




# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    email = models.EmailField(default='', max_length=100)
    whatsapp = models.CharField(max_length=100, default="Введите ссылку")
    telegram =  models.CharField(max_length=100, default="Введите ссылку")
    instagram = models.CharField(max_length=100, default="Введите ссылку")

    def __str__(self):
         return self.name









class Stats(models.Model):
    students = models.IntegerField(default=0)
    graduates = models.IntegerField(default=0)
    employees = models.IntegerField(default=0)
    meetings = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='stats')

    def __str__(self):
         return self.name








