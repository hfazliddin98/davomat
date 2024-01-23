from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Talaba, Fakultet

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'last_name', 'first_name', 'lavozim']
    

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'sharif', 'fakultet']

@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display = ['id', 'yonalish', 'kurs', 'guruh']
