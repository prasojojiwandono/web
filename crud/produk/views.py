from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def index(request):
	ContentProduct = models.produk.objects.all()
	content ={
				'judul' : 'produk',
				'body'	: ContentProduct,
			
	}
	x = range(1,6)
	print('haha hihi huhu')
	print(x)

	return render(request,'produk/index.html',content)

def create(request):
	produk_form = forms.ProdukForm(request.POST or None)
	if request.method == 'POST':
		if produk_form.is_valid():

			# ada 2 cara : 

			# yang pertama
			# models.produk.objects.create(
			# 	NamaProduct = produk_form.cleaned_data.get('NamaProduct'),
			# 	DeskripsiProduct = produk_form.cleaned_data.get('DeskripsiProduct'),
			# 	Tipe = produk_form.cleaned_data.get('Tipe'),
			# 	)

			# yang kedua
			produk_form.save()

			return redirect('produk:home')
	content = {
			'judul':'buat produk',
			'produk_form':produk_form

	}
	return render(request,'produk/create.html',content)

def delete(request,id):
	models.produk.objects.filter(id=id).delete()
	return redirect('produk:home')

def update(request,id):
	objekupdate = models.produk.objects.get(id=id)
	data = {
		'NamaProduct':objekupdate.NamaProduct,
		'DeskripsiProduct': objekupdate.DeskripsiProduct,
		'Tipe':objekupdate.Tipe,
	}
	objekform = forms.ProdukForm(request.POST or None,initial=data,instance=objekupdate)

	if request.method == 'POST':
		if objekform.is_valid():

			# ada 2 cara : 

			# yang pertama
			# models.produk.objects.create(
			# 	NamaProduct = produk_form.cleaned_data.get('NamaProduct'),
			# 	DeskripsiProduct = produk_form.cleaned_data.get('DeskripsiProduct'),
			# 	Tipe = produk_form.cleaned_data.get('Tipe'),
			# 	)

			# yang kedua
			objekform.save()

			return redirect('produk:home')
	content = {
			'judul':'update produk',
			'produk_form':objekform

	}
	return render(request,'produk/create.html',content)


