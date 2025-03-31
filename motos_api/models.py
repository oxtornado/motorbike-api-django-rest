from django.db import models

# Create your models here.
<<<<<<< HEAD

class Moto(models.Model):
    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=60, blank=False, null=False)
    trademark = models.CharField(max_length=60, blank=False, null=False)
    model = models.CharField(max_length=4, blank=False, null=False)
    price = models.IntegerField()
    image = models.CharField(max_length=150, blank=False, null=False)
    supplier = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.reference
=======
>>>>>>> a3319ba (initialize Django project structure with basic settings and configurations)
