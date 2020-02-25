from django.db import models

# Create your models here.
class Ana_sehife_Sekil(models.Model):
	img=models.ImageField()
	def __str__(self):
		return "Ana sehife karusel sekili"


class Xidmetler_Sekil(models.Model):
	img=models.ImageField()
	def __str__(self):
		return "Xidmetler seyfesi sekili"

class Haqqimizda_Sekil(models.Model):
	img=models.ImageField()
	def __str__(self):
		return "Haqqimizda seyfesi sekili"


class Haqqimizda_basliq(models.Model):
	header=models.TextField()


class Haqqimizda_melumatlari(models.Model):
	sadalanan_melumatlar=models.TextField()


class Elaqe_Sekil(models.Model):
	img=models.ImageField()
	def __str__(self):
		return "Elaqe seyfesi sekili"


class Elaqe_melumatlari(models.Model):
	address=models.CharField(max_length=255)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField()
	website=models.CharField(max_length=250)