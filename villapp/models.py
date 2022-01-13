from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Profile(models.Model): #HABITANTES!!
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name = 'Profile')
    nombre = models.CharField(max_length=300, null =True)
    apellido = models.CharField(max_length=300, null =True)
    casaN = models.CharField(max_length=40, null =  True)
    cedula = models.CharField(max_length=40, null =  True)

    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
        
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


class Categories(models.TextChoices):
    ENERO =  'Enero'
    FEBRERO = 'Febrero'
    MARZO = 'Marzo'
    ABRIL = 'Abril'
    MAYO = 'Mayo'
    JUNIO = 'Junio'
    JULIO = 'Julio'
    AGOSTO = 'Agosto'
    SEPTIEMBRE = 'Septiembre'
    OCTUBRE = 'Octubre'
    NOVIEMBRE = 'Noviembre'
    DICIEMBRE = 'Diciembre'
    

class Deudas(models.Model):
    nombreD = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'Deudas')
    mes = models.CharField(
        max_length=50, choices=Categories.choices, default=Categories.ENERO)
    pago_dolares = models.DecimalField(max_digits=8, decimal_places=2)
    pago_bolivares = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.nombreD.username