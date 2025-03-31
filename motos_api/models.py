from django.db import models

# Create your models here.

class Moto(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=60, blank=False, null=False)
    trademark = models.CharField(max_length=60, blank=False, null=False)
    model = models.CharField(max_length=4, blank=False, null=False)
    price = models.IntegerField()
    image = models.ImageField(max_length=150, blank=False, null=False)
    supplier = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.reference