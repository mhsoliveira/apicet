from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
import json

# Create your views here.

from rest_framework import viewsets

from .serializers import OCRSerializer
from .models import OCR


class OCRViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OCR.objects.all().order_by('data')
    serializer_class = OCRSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return HttpResponse(json.dumps(serializer.data, ensure_ascii=False), content_type="application/json")
