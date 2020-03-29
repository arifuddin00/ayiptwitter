from django.db import models

# Create your models here.
class Profil(models.Model):
	nama = models.CharField('Nama', max_length=50)
	umur = models.IntegerField('Umur')
	emel = models.EmailField('Email')

	def __str__(self):
		return self.nama