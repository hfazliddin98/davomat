from django.contrib import admin
from .models import Davomat


@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ['id', 'talaba_id', 'bor', 'yoq', 'amaliyot']


