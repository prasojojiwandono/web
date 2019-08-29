from django.shortcuts import render,redirect
from .models import karyawan
from .forms import formkaryawan
from django.core.validators import validate_email

# Create your views here.
def index(request):
	emp = karyawan.objects.all()
	content ={
				'judul' : 'karyawan',
				'isi'	: emp
	}
	return render(request,'karyawan/index.html',content)

def create(request):
	karyawanbaru = formkaryawan(request.POST or None)# ini harus di definisikan terlebih dahulu

	if request.method =='POST':

		if karyawanbaru.is_valid():
			karyawanbaru.save()
			return redirect('karyawan:home')
		
	
	# isikaryawan = formkaryawan()	
	content = {
			'judul':'karyawan baru',
			'karyawan_form':karyawanbaru

	}
	return render(request,'karyawan/create.html',content)

def delete(request,id):
	karyawan.objects.get(id=id).delete()
	return redirect('karyawan:home')

def update(request,id):
	objekupdate = karyawan.objects.get(id=id)
	data={
		'Nama':objekupdate.Nama,
		'Alamat':objekupdate.Alamat,
		'Tgl_lahir':objekupdate.Tgl_lahir,
		'Nomor HP':objekupdate.Telpon,# nomor HP disini adalah labelnya
		'Email':objekupdate.Email,
		'Gender':objekupdate.Gender
	}
	objekform = formkaryawan(request.POST or None,initial=data,instance=objekupdate)
	if request.method == 'POST':
		if objekform.is_valid():
			objekform.save()
			return redirect('karyawan:home')

	content = {
			'judul':'update karyawan',
			'karyawan_form':objekform

	}
	return render(request,'karyawan/create.html',content)
