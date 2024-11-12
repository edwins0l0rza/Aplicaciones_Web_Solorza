from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=8)
    direccion = models.IntegerField()

    def __str__(self):
        return f"Usuario {self.usuario}"
    
class Producto(models.Model):
    cod_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    referencia = models.CharField(max_length=8)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=60)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    

    #llave foranea
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre})"
