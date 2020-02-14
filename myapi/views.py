from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework import viewsets

from .serializers import OCRSerializer
from .models import OCR


class OCRViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OCR.objects.all().order_by('data')
    serializer_class = OCRSerializer
