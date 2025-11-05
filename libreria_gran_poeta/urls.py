from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('inventario.urls', namespace="productos")),

    # Autenticación (login / logout)
    path('cuentas/', include('django.contrib.auth.urls')),

    # Redirección automática desde la raíz
    path('', lambda request: redirect('productos:list')),
]
