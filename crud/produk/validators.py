from django.core.exceptions import ValidationError
import re


def ValidNamaProduk(value):
	x = re.search("'",value)
	if (x):
		pesan_error ="maaf tidak bisa memakai tanda kutip (')"
		raise ValidationError(pesan_error)
