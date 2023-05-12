from django.urls import path
from main.views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('panel/', Panel.as_view(), name='panel'),
    path('productos/', Productos.as_view(), name='productos'),
    path('prefacturas/', Prefactura.as_view(), name='prefacturas'),
]
