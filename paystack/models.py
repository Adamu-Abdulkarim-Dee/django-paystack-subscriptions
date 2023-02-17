from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class PaymentHistory(models.Model):
    pass
