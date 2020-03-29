from django.db import models

class Profil(models.Model):
	nama = models.CharField('Nama', max_length=50)
	umur = models.IntegerField('Umur')
	emel = models.EmailField('Email')

	def __str__(self):
		return self.nama