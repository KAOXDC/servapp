from django.shortcuts import render
from rest_framework import viewsets
from servicios.models import *
from .serializers import *

# class producto_viewset (viewsets.ModelViewSet):
# 	queryset = Producto.objects.all()
# 	serializer_class = producto_serializer

class Obra_viewset (viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = Obra_serializer 

class Elemento_viewset (viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = Elemento_serializer 

class ElementoObra_viewset (viewsets.ModelViewSet):
    queryset = ElementoObra.objects.all()
    serializer_class = ElementoObra_serializer 

class Enfermedad_viewset (viewsets.ModelViewSet):
    queryset = Enfermedad.objects.all()
    serializer_class = Enfermedad_serializer 

class Medicamento_viewset (viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = Medicamento_serializer 

class Categoria_viewset (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = Categoria_serializer 

class Producto_viewset (viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_serializer 

class TipoMensaje_viewset (viewsets.ModelViewSet):
    queryset = TipoMensaje.objects.all()
    serializer_class = TipoMensaje_serializer 

class Mensaje_viewset (viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = Mensaje_serializer 

class Material_viewset (viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = Material_serializer 

class Manualidad_viewset (viewsets.ModelViewSet):
    queryset = Manualidad.objects.all()
    serializer_class = Manualidad_serializer 

class Autor_viewset (viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_serializer 

class Libro_viewset (viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Libro_serializer 

class TipoModular_viewset (viewsets.ModelViewSet):
    queryset = TipoModular.objects.all()
    serializer_class = TipoModular_serializer 

class Modular_viewset (viewsets.ModelViewSet):
    queryset = Modular.objects.all()
    serializer_class = Modular_serializer 

class tipoVehiculo_viewset (viewsets.ModelViewSet):
    queryset = tipoVehiculo.objects.all()
    serializer_class = tipoVehiculo_serializer 

class Vehiculo_viewset (viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = Vehiculo_serializer 

class tipoTramite_viewset (viewsets.ModelViewSet):
    queryset = tipoTramite.objects.all()
    serializer_class = tipoTramite_serializer 

class Tramite_viewset (viewsets.ModelViewSet):
    queryset = Tramite.objects.all()
    serializer_class = Tramite_serializer 

class Propietario_viewset (viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = Propietario_serializer 

class Carro_viewset (viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = Carro_serializer 

class Marca_viewset (viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = Marca_serializer 

class Motocicleta_viewset (viewsets.ModelViewSet):
    queryset = Motocicleta.objects.all()
    serializer_class = Motocicleta_serializer 

class TipoDocumento_viewset (viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumento_serializer 

class Documento_viewset (viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = Documento_serializer 

class TipoComida_viewset (viewsets.ModelViewSet):
    queryset = TipoComida.objects.all()
    serializer_class = TipoComida_serializer 

class Comida_viewset (viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = Comida_serializer 
