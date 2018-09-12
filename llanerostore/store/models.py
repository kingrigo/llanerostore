from django.db import models

# Create your models here.
class Item(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    compatibilidad = models.CharField(max_length=100,blank=True)
    estado = models.CharField(max_length=50,blank=True)
    precio = models.FloatField(default=0)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

    def getImg(self):
        img = self.foto_set.get(orden=1)
        return img.imagen.url
    

class Foto(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    orden = models.IntegerField()
    imagen = models.ImageField()
    



    