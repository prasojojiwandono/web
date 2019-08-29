from django.urls import path
from . import views


app_name = 'produk'

urlpatterns=[
	path('',views.index,name ='home'),
	path('create/',views.create,name ='create'),
	path('delete/<id>/',views.delete,name ='delete'),
	path('update/<id>/',views.update,name ='update'),
]