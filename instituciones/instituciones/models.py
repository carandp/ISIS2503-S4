from django.db import models

class Factura(models.Model):
    institucion= models.TextField(primary_key=True)
    direccion= models.TextField()
    nombre= models.TextField()
    telefono= models.TextField()
    correo= models.TextField()

    def __str__(self):
        return f"{self.institucion} guardada exitosamente - Contacto: {self.nombre}"

