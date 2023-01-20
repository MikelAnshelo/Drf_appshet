from django.db import models

# Create your models here.
class productos(models.Model):
	Codigo = models.CharField(max_length=200)
	Descripcion = models.TextField()
	precios = models.CharField(max_length=200)
	Rubro = models.CharField(max_length=200)
	Subrubro = models.CharField(max_length=200)
	Presentacion = models.CharField(max_length=200)