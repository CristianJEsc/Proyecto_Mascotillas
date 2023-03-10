from django.shortcuts import render
from Mascotillas.models import *
from django.http import HttpResponse
from Mascotillas.forms import *

def home(request):
    return render(request,'Mascotillas/home.html')

def mascotas(request):
    if request.method == 'POST':
        mascotas_formulario = MascotasFormulario(request.POST)
        print(mascotas_formulario)
        if mascotas_formulario.is_valid:

            informacion= mascotas_formulario.cleaned_data
            mascota = Mascotas(animal=informacion['animal'],
                                raza=informacion['raza'],
                                nombre=informacion['nombre'],
                                fecha_nacimiento=informacion['fecha_nacimiento'],)
            mascota.save()
            return render(request, 'Mascotillas/home.html')
    else:
        mascotas_formulario = MascotasFormulario()

    return render(request,'Mascotillas/mascotas.html',{'mascotas_formulario':mascotas_formulario})

def servicios(request):
    if request.method == 'POST':
        servicios_formulario = ServiciosFormulario(request.POST)
        print(servicios_formulario)
        if servicios_formulario.is_valid:

            informacion= servicios_formulario.cleaned_data
            servicios = Servicios(nombre=informacion['nombre'],
                                precio=informacion['precio'],)

            servicios.save()
            return render(request, 'Mascotillas/home.html')
    else:
        servicios_formulario = ServiciosFormulario()

    return render(request,'Mascotillas/servicios.html',{'servicios_formulario':servicios_formulario})

def productos(request):
    if request.method == 'POST':
        productos_formulario = ProductosFormulario(request.POST)
        print(productos_formulario)
        if productos_formulario.is_valid:

            informacion= productos_formulario.cleaned_data
            servicios = Productos(nombre=informacion['nombre'],
                                marca=informacion['marca'],
                                precio=informacion['precio'],)

            servicios.save()
            return render(request, 'Mascotillas/home.html')
    else:
        productos_formulario = ProductosFormulario()

    return render(request,'Mascotillas/productos.html',{'productos_formulario':productos_formulario})

def buscarMascota(request):
    return render(request,'Mascotillas/buscarMascota.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        mascotas= Mascotas.objects.filter(nombre__icontains=nombre)
        return render(request,"Mascotillas/home.html", {"mascota":mascotas,"nombre":nombre})
    else:
        respuesta="No enviaste datos"
    return render(request,"home.html",{"respuesta":respuesta})
    

