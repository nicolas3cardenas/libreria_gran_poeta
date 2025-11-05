from django.db import models
from django.contrib.auth.models import User

# --- MODELO EDITORIAL ---
class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nombre


# --- MODELO AUTOR ---
class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nombre


# --- MODELO BODEGA ---
class Bodega(models.Model):
    nombre = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=200, blank=True)
    capacidad_maxima = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre


# --- MODELO PRODUCTO ---
class Producto(models.Model):
    TIPO_CHOICES = [
        ('LIBRO', 'Libro'),
        ('REVISTA', 'Revista'),
        ('UTIL', 'Útil Escolar'),
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, null=True, blank=True)
    isbn = models.CharField(max_length=30, unique=True)
    anio_publicacion = models.PositiveIntegerField(null=True, blank=True)
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.isbn})"


# --- MODELO MOVIMIENTO ---
class Movimiento(models.Model):
    TIPO_MOV = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('TRASLADO', 'Traslado'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_MOV)
    bodega_origen = models.ForeignKey(Bodega, on_delete=models.PROTECT, related_name='movimientos_salida', null=True, blank=True)
    bodega_destino = models.ForeignKey(Bodega, on_delete=models.PROTECT, related_name='movimientos_entrada', null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} {self.cantidad} x {self.producto.nombre} ({self.fecha:%Y-%m-%d})"
