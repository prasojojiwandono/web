from django.db import models
from django.core.validators import validate_email
from .validators import NomorIndonesia
# Create your models here.
class karyawan(models.Model):
	Nama = models.CharField(max_length=200)
	Telpon =models.CharField(max_length=15, validators=[NomorIndonesia])
	Alamat = models.TextField()
	Email = models.EmailField(
			# validators=[validate_email],
		)
	Jenis_kelamin=[
			('P','Pria'),
			('W','Wanita'),
	]
	Gender =models.CharField(max_length=2, choices=Jenis_kelamin)
	Tgl_lahir = models.DateField()

	def __str__(self):
		return '{}'.format(self.Nama)


