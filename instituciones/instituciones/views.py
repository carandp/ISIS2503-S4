from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import FacturaForm
from .logic.factura_logic import get_facturas, create_factura
from django.contrib.auth.decorators import login_required
# Descomentar cuando se cree el archivo monitoring/auth0backend.py
from monitoring.auth0backend import getRole
from .decorators import admin_required


@login_required
@admin_required
def factura_list(request):
    role = getRole(request)
    if role == "admin":
        facturas = get_facturas()
        context = {
            'facturas_list': facturas
        }
        return render(request, 'Factura/factura.html', context)
    else:
        # Redirect me to /logout when I'm not an admin
        return HttpResponse("Unauthorized User")

@login_required
@admin_required
def factura_create(request):
    role = getRole(request)
    if role == "admin":
        if request.method == 'POST':
            form = FacturaForm(request.POST)
            if form.is_valid():
                create_factura(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created factura')
                return HttpResponseRedirect(reverse('facturaCreate'))
            else:
                print(form.errors)
        else:
            form = FacturaForm()

        context = {
            'form': form,
        }
        return render(request, 'Factura/facturaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")