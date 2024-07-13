from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Servicios
from django.urls import reverse
# Create your views here. \


def index(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/index.html', {'servicios': servicios})

def crud(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/servicios_lista.html', {'servicios': servicios})

def serviciosAdd(request):
    if request.method == "POST":
        servicio = request.POST["servicio"]
        valor = request.POST["valor"]
        mecanico = request.POST["mecanico"]
        descripcion = request.POST["descripcion"]
        activo = True 

        obj = Servicios.objects.create(
            servicio=servicio,
            valor=valor,
            mecanico=mecanico,
            descripcion=descripcion,
            activo=activo
        )

        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'servicios/servicios_add.html', context)
    else:
        servicios = Servicios.objects.all()
        return render(request, 'servicios/servicios_add.html', {'servicios': servicios})
       
def servicios_del(request, pk):
    servicio = get_object_or_404(Servicios, pk=pk)
    servicio.delete()
    mensaje = "OK, datos eliminados..."
    
    servicios = Servicios.objects.all()
    context = {'servicios': servicios, 'mensaje': mensaje}
    return render(request, 'servicios/servicios_lista.html', context)

    
def servicios_findEdit(request, pk):
    servicio = get_object_or_404(Servicios, id=pk)
    context = {'servicio': servicio}
    return render(request, 'servicios/servicios_edit.html', context)
    
def serviciosUpdate(request, pk):
    servicio = get_object_or_404(Servicios, id=pk)
    if request.method == "POST":
        servicio.servicio = request.POST["servicio"]
        servicio.valor = request.POST["valor"]
        servicio.mecanico = request.POST["mecanico"]
        servicio.descripcion = request.POST["descripcion"]
        servicio.activo = True
        servicio.save()
        context = {'mensaje': "Ok, datos actualizados...", 'servicio': servicio}
        return render(request, 'servicios/servicios_edit.html', context)
    else:
        return redirect('servicios_findEdit', pk=pk)