from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'last_name', 'first_name', 'lavozim']
    


