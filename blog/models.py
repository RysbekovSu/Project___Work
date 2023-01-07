from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title


class Home(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField(default='No data')
    email = models.CharField(default='', max_length=100)
    telephonenumber = models.CharField(max_length=100, default='(+996)-123-456-789')
    address = models.CharField(default='Maldybaeva 34b  ', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name




class Footer(models.Model):
    Address= models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.URLField(max_length=100)
    Addressurl = models.CharField(max_length=100)
    def __str__(self):
        return self.Address


# class ProgLangForms(forms.Modelform):
#     class Meta:
#         model=models.