from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Talaba

admin.site.unregister(Group)


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fish', 'yonalish', 'kurs', 'guruh']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'last_name', 'first_name', 'lavozim']
    
