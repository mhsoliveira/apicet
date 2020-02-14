from rest_framework import serializers

from .models import OCR

class OCRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OCR
        fields = ('placa', 'porte', 'data', 'codigocet', 'velocidade')
