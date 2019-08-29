from django.db import models
from .validators import ValidNamaProduk

# Create your models here.
class produk(models.Model):
	NamaProduct = models.CharField(
						max_length=255,
						validators=[ValidNamaProduk]
						)
	DeskripsiProduct = models.CharField(
						max_length=255,
						blank=True
						)
	pilihan_tipe = [
			('A','Tipe A'),
			('B','Tipe B'),
			('C','Tipe C'),
	]
	Tipe = models.CharField(
						max_length=10, 
						choices=pilihan_tipe
						)
	CreateDate =models.DateField(auto_now_add=True)
	UpdateDate =models.DateField(auto_now=True)

	def __str__(self):
		return '{}. {}'.format(self.id,self.NamaProduct)



