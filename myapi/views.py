from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import OCRSerializer
from .models import OCR


class OCRViewSet(viewsets.ModelViewSet):
    queryset = OCR.objects.all().order_by('data')
    serializer_class = OCRSerializer
