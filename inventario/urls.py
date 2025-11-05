from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    movimiento_crear,  
    MovimientoListView,
)

app_name = "productos"

urlpatterns = [
    path('', ProductoListView.as_view(), name='list'),
    path('crear/', ProductoCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar'),
    path('movimiento/', movimiento_crear, name='movimiento'),
    path('movimientos/', MovimientoListView.as_view(), name='movimiento_list'),  

]
