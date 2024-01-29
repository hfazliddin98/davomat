from django.urls import path
from .views import attendance_detail, attendance_take, attendance_update, baza, kunlik



urlpatterns = [    
    path('<int:team_id>/attendance/', attendance_detail, name='detail'),
    path('<int:team_id>/attendance/take/', attendance_take, name='take'),
    path('<int:attendance_id>/attendance/update/', attendance_update, name='update'),
    path('baza/', baza, name='baza'),
    path('kunlik/', kunlik, name='kunlik'),
]