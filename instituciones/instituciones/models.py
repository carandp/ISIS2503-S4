from django.db import models

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField()
    descripcion = models.TextField()
    total = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

        data = {
            'title': 'Factura: ' + str(self.pk),
            'body': self.total,
            'userId': self.cedula,
        }

        # api_url = 'https://jsonplaceholder.typicode.com/posts'
        # response = requests.post(api_url, json=data, headers={'Content-type': 'application/json; chars>

        # if response.status_code == 201:
            # print('Data posted successfully')
        # else:
            # super().delete(*args, **kwargs)
            # print(f'Failed to post data: {response.status_code} - {response.text}')

    def __str__(self):
        return f"ID Factura: {self.pk} TOTAL: {self.total}"

