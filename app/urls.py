from django.urls import path
from  .views import *
 
urlpatterns = [
    path('', index, name='home'),
    path('add/', add_spice, name='add_spice'),
     
     
    
]