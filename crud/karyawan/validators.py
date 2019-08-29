from django.core.exceptions import ValidationError
import re


def NomorIndonesia(value):
	
	
	m = re.search('^(\+62)\d+$',value)
	n = re.search('^0\d+$',value)
	if (m or n):
		pass
	else:
		pesan_error ='masukan nomor HP yang valid'
		raise ValidationError(pesan_error)
	
