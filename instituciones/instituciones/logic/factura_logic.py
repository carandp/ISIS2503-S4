from ..models import Factura

def get_facturas():
    queryset = Factura.objects.all()
    return (queryset)
"""
def get_variable(id):
    Factura = Factura.objects.raw("SELECT * FROM variables_variable WHERE id=%s" % id)[0]
    return (Factura)
"""
def create_factura(form):
    measurement = form.save()
    measurement.save()
    return ()