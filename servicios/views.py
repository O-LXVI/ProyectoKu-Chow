from django.shortcuts import render


from .models import Servicios
# Create your views here. \



def index(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/index.html', {'servicios': servicios})

def crud(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/servicios_lista.html', {'servicios': servicios})

def serviciosAdd(request):
    if request.method is not "POST":
        servicios = Servicios.objects.all()
        return render(request, 'servicios/servicios_add.html', {'servicios': servicios})
    else:
        servicio=request.POST["servicio"]
        valor=request.POST["valor"]
        mecanico=request.POST["mecanico"]
        descripcion=request.POST["descripcion"]
        activo="1"

        obj=Servicios.objects.create(  servicio=servicio,
                                       valor=valor,
                                       mecanico=mecanico,
                                       descripcion=descripcion,
                                       activo=1)
        obj.save()
        context={'mensaje': "OK, datos grabados..."}
        return render(request, 'servicios/servicios_add.html', {'servicios': servicios})
    
def servicios_del(request,pk):
    try:
        servicio=Servicios.objects.get(Servicio=pk)
        
        servicio.delete()
        mensaje="OK, datos eliminados..."
        servicio= Servicios.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
    except:
        mensaje="Error, servicio no existente..."
        servicios=Servicios.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
        return render(request, 'servicios/servicios_lista.html', {'servicios': servicios})
    
def servicios_findEdit(request,pk):
    if pk != "":
        servicio=Servicios.objects.get(Servicio=pk)
        servicio=Servicios.objects.all()
        if servicio:
            return render(request, 'servicios/servicios_edit.html', {'servicios': servicios})