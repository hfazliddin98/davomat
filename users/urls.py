from django.urls import path
from .views import kirish, home, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),    
    path('logout/', logout_view, name='logout'),    
]