from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi
class Maxsulot(models.Model):
    nomi = models.CharField(max_length=20)
    narxi = models.IntegerField()
    rasm = models.CharField(max_length=200)
    malumot = models.TextField()
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)

class Korzinka(models.Model):
    nomi = models.CharField(max_length=20)
    narxi = models.IntegerField()
    rasm = models.CharField(max_length=200)
    son = models.DecimalField(max_digits=100,decimal_places=2,default=1)
    tg_id = models.IntegerField()
    ism = models.CharField(max_length=50)
