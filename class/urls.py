from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home page'),
    path('about/', views.about, name='about'),
    path('login/',views.login, name='login'),
    path('contact/',views.contact, name ='contact')

]