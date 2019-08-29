from django.shortcuts import render
import datetime




def index(request):
	x=datetime.datetime.now()
	content = {
				'waktu':x,
				'judul' : 'home'
				}
	return render(request,'index.html',content)