from django.contrib import admin
from .models import Davomat, Baza


@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ['id', 'fakultet']


@admin.register(Baza)
class BazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'davomat', 'talaba']


