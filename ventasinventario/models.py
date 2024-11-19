from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    nombre = models.CharField(max_length=50)
    rol = models.CharField(max_length=13, verbose_name='Rol administrador/jefe de bodega')
    user = models.OneToOneField(User, on_delete= models.RESTRICT)
    
    def __str__(self) -> str:
        return f'{self.nombre}'
    
class JefeBodega(models.Model):
    nombre = models.CharField(max_length=50)
    rol = models.CharField(max_length=12)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    descripcion = models.TextField(blank= True, null=True)
    imagen = models.ImageField(blank=True, null=True, upload_to='media')
    
    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    montoRecibido = models.IntegerField()
    producto = models.ManyToManyField(Producto)
    administrador = models.ForeignKey(Administrador, blank=True, null= True, on_delete= models.RESTRICT )
    