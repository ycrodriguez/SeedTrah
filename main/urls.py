from django.urls import path
from django.contrib.auth.decorators import login_required

from main.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('panel/', login_required(Panel.as_view()), name='panel'),
    path('productos/', login_required(ProductosView.as_view()), name='productos'),
    path('prefacturas/', login_required(PrefacturaView.as_view()), name='prefacturas'),
    path('add_cliente/', login_required(AddCliente.as_view()), name='add_cliente'),
    path('add_prefactura/<int:pk>/', login_required(AddPrefactura.as_view()), name='add_prefactura'),
    path('delete_prefactura/<int:pk>/', login_required(DeletePrefactura.as_view())),
    path('delete_cuenta/', login_required(DeleteCuenta.as_view()), name='delete_cuenta')
]
