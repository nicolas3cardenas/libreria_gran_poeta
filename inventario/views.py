# -------------------------------------------------------------
# Librería El Gran Poeta - Vistas de la aplicación "inventario"
# -------------------------------------------------------------

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Producto, Movimiento, Bodega


# ------------------- CRUD de Productos ------------------------

class ProductoListView(ListView):
    model = Producto
    template_name = "inventario/producto_list.html"
    context_object_name = "productos"


class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'tipo', 'editorial', 'autor', 'isbn', 'anio_publicacion', 'bodega', 'stock']
    template_name = "inventario/producto_form.html"
    success_url = reverse_lazy('productos:list')


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'tipo', 'editorial', 'autor', 'isbn', 'anio_publicacion', 'bodega', 'stock']
    template_name = "inventario/producto_form.html"
    success_url = reverse_lazy('productos:list')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "inventario/producto_confirm_delete.html"
    success_url = reverse_lazy('productos:list')


# ------------------- Movimientos de Inventario ------------------------

@login_required
def movimiento_crear(request):
    """
    Permite registrar un movimiento de inventario (entrada, salida, traslado)
    actualizando el stock del producto correspondiente.
    """
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        tipo = request.POST.get('tipo')
        origen_id = request.POST.get('bodega_origen') or None
        destino_id = request.POST.get('bodega_destino') or None
        cantidad = int(request.POST.get('cantidad', 0))

        producto = get_object_or_404(Producto, pk=producto_id)

        # 🔹 Lógica básica de stock
        if tipo == 'ENTRADA':
            producto.stock += cantidad
        elif tipo == 'SALIDA':
            producto.stock = max(0, producto.stock - cantidad)
        elif tipo == 'TRASLADO':
            producto.stock = max(0, producto.stock - cantidad)

        producto.save()

        Movimiento.objects.create(
            producto=producto,
            tipo=tipo,
            bodega_origen=Bodega.objects.get(pk=origen_id) if origen_id else None,
            bodega_destino=Bodega.objects.get(pk=destino_id) if destino_id else None,
            cantidad=cantidad,
            usuario=request.user
        )

        # 🔁 redirige al historial de movimientos (flujo más intuitivo)
        return redirect('productos:movimiento_list')

    context = {
        'productos': Producto.objects.all(),
        'bodegas': Bodega.objects.all(),
    }
    return render(request, 'inventario/movimiento_form.html', context)


# ------------------- Historial de Movimientos ------------------------

@method_decorator(login_required, name='dispatch')
class MovimientoListView(ListView):
    """
    Muestra una tabla con todos los movimientos de inventario registrados.
    """
    model = Movimiento
    template_name = "inventario/movimiento_list.html"
    context_object_name = "movimientos"
    ordering = ['-fecha']  # más recientes primero
