from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('reservacion/', views.reservacion, name='Reservacion'),
    path('faqs/', views.faqs, name='Faqs'),
    path('contacto/', views.contacto, name='Contacto'),
    path('albercas/', views.albercas, name='Albercas'),
    path('naturales/', views.areas, name='Areas'),
]
