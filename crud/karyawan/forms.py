from django import forms
from .models import karyawan
import datetime


class formkaryawan(forms.ModelForm):
    class Meta:
        model = karyawan
        fields = (
        	'Nama',
        	'Telpon',
        	'Alamat',
        	'Email',
        	'Tgl_lahir',
        	'Gender',
        	)
        x = datetime.datetime.now()
        y = x.year
        widgets= {
        	'Tgl_lahir':forms.SelectDateWidget(years=[i for i in range(y-60,y)])
        }
        labels={
        'Telpon':'Nomor HP',
        }

   
