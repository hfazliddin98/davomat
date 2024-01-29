from django.contrib import admin
from .models import Yonalish, Kurs, Guruh
from .models import Team, Worker, Attendance, Mark 


class WorkerInline(admin.TabularInline):
    model = Worker 

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [WorkerInline]
    list_display = ['id', 'yonalish', 'kurs', 'guruh']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'date']

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'sharif', 'team']

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'attendance', 'worker']


@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
