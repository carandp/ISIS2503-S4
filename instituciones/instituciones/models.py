from django.db import models

class Factura(models.Model):
    institucion= models.TextField(primary_key=True)
    direccion= models.TextField()
    nombre= models.TextField()
    telefono= models.TextField()
    correo= models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.institucion} guardada exitosamente - Contacto: {self.nombre}"

