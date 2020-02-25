
from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.home, name='etna-home'),
    path('services/', views.services, name='etna-services'),
    path('about/', views.about, name='etna-about'),
    path('contact/', views.contact, name='etna-contact')
]


