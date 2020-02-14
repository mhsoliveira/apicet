from django.db import models

# Create your models here.

# models.py

class OCR(models.Model):
    placa = models.CharField(max_length=60)
    porte = models.CharField(max_length=60)
    data = models.CharField(max_length=60)
    codigocet = models.CharField(max_length=60)
    velocidade = models.CharField(max_length=60)

    def __str__(self):
        return self.placa
