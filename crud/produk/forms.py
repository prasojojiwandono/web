from django import forms
from .models import produk

class ProdukForm(forms.ModelForm):
	class Meta:
		model = produk #mengacu pada class produk di models.py
		fields =[
			'NamaProduct',
			'DeskripsiProduct',
			'Tipe',
		]


	