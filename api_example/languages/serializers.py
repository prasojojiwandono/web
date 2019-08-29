from rest_framework import serializers
from .models import Languages

class LanguagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Languages
		fields = ('id','name','paradigm')
		