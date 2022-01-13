from django.contrib import admin
from .models import Profile, Deudas


class ProfileAdmin (admin.ModelAdmin):
    model = Profile
    list_display = ('nombre', 'apellido', 'casaN')

class DeudasAdmin(admin.ModelAdmin):
    model = Deudas
    list_display = ('nombreD' , 'mes', 'pago_dolares', 'pago_bolivares', 'date_created')


# Register your models here.
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Deudas, DeudasAdmin)