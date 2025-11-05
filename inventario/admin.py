from django.contrib import admin
from .models import Editorial, Autor, Bodega, Producto, Movimiento

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'capacidad_maxima')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'editorial', 'autor', 'isbn', 'bodega', 'stock')
    search_fields = ('nombre', 'isbn')
    list_filter = ('tipo', 'bodega', 'editorial')

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'producto', 'cantidad', 'fecha', 'usuario')
    list_filter = ('tipo', 'fecha')
