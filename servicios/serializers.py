
from rest_framework import serializers
from servicios.models import *

# class producto_serializer_serializer (serializers.ModelSerializer):
# 	class Meta:
# 		model = Producto 
# 		fields = ('id', 'nombre', 'precio', 'foto', 'status', 'marca', 'categoria')
		

class Obra_serializer (serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'
        
class Elemento_serializer (serializers.ModelSerializer):
    class Meta:
        model = Elemento
        fields = '__all__'
        
class ElementoObra_serializer (serializers.ModelSerializer):
    class Meta:
        model = ElementoObra
        fields = '__all__'
        
class Enfermedad_serializer (serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = '__all__'
        
class Medicamento_serializer (serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'
        
class Categoria_serializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class Producto_serializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class TipoMensaje_serializer (serializers.ModelSerializer):
    class Meta:
        model = TipoMensaje
        fields = '__all__'
        
class Mensaje_serializer (serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'
        
class Material_serializer (serializers.ModelSerializer):
    class Meta:
        model = Material

        fields = '__all__'
        
class Manualidad_serializer (serializers.ModelSerializer):
    class Meta:
        model = Manualidad
        fields = '__all__'
        
class Autor_serializer (serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        
class Libro_serializer (serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
        
class TipoModular_serializer (serializers.ModelSerializer):
    class Meta:
        model = TipoModular
        fields = '__all__'
        
class Modular_serializer (serializers.ModelSerializer):
    class Meta:
        model = Modular
        fields = '__all__'
        
class tipoVehiculo_serializer (serializers.ModelSerializer):
    class Meta:
        model = tipoVehiculo
        fields = '__all__'
        
class Vehiculo_serializer (serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class tipoTramite_serializer (serializers.ModelSerializer):
    class Meta:
        model = tipoTramite
        fields = '__all__'
        
class Tramite_serializer (serializers.ModelSerializer):
    class Meta:
        model = Tramite
        fields = '__all__'
        
class Propietario_serializer (serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'
        
class Carro_serializer (serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'
        
class Marca_serializer (serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
        
class Motocicleta_serializer (serializers.ModelSerializer):
    class Meta:
        model = Motocicleta
        fields = '__all__'
        
class TipoDocumento_serializer (serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'
        
class Documento_serializer (serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'
        
class TipoComida_serializer (serializers.ModelSerializer):
    class Meta:
        model = TipoComida
        fields = '__all__'
        
class Comida_serializer (serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'
        