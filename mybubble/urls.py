from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .views import index,registro,recover, signIn , recuperar,updateDatos,bubble
from . import views
urlpatterns = [
    path('', signIn, name="index"),
    path('registro', registro, name="registro"),
    path('recover', recover, name="recover"),
    path('calendario', LoginView.as_view(), name='calendario'),
    path('micuenta', LoginView.as_view(), name='micuenta'),
    path('inicio', LoginView.as_view(), name='inicio'),
    path('recuperar', recuperar, name="recuperar"),
    path('updateDatos', updateDatos, name="updateDatos"),
    path('bubble', bubble, name="bubble"),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata')
    
    
    

    

]

