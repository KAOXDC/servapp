from django.db import models
from django.contrib.auth.models import User



# Milton 
# 	Productos por Obra, para modificar  precios en la TABLA DE RELACION
# 	Producto -- ProductoObra -- Obra
################################## Proyecto Obra ############################################
class Obra (models.Model):
    nombre          = models.CharField(max_length=200)
    cliente         = models.CharField(max_length=200, null = True , blank = True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)

    def __str__ (self):
        return nombre

class Elemento (models.Model):
    nombre          = models.CharField(max_length=200)
    description     = models.TextField()
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)

    def __str__ (self):
        return nombre

class ElementoObra (models.Model):
    nombre          = models.CharField(max_length=200)
    precio          = models.IntegerField()
    cantidad        = models.IntegerField()
    obra            = models.ForeignKey(Obra, models.PROTECT)
    elemento        = models.ForeignKey(Elemento, models.PROTECT)

    def __str__ (self):
        return nombre



################################## Proyecto Naturista ############################################
# Lenin Montilla
# 	Tienda Naturista relaciona Productos con las enfermedades
# 	Producto -- ProductoEnfermedad -- Enfermedad


class Enfermedad (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Medicamento (models.Model):
    nombre          = models.CharField(max_length=200)
    description     = models.TextField()
    precio          = models.IntegerField()
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    enfermedad      = models.ManyToManyField(Enfermedad, null = True, blank = True) 
    def __str__ (self):
        return nombre


################################## Proyecto Cafeteria ############################################
# Laura
# 	Productos de una cafeteria y su categoria

class Categoria (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Producto (models.Model):
    nombre          = models.CharField(max_length=200)
    precio          = models.IntegerField()
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    categoria       = models.ForeignKey(Categoria, on_delete = models.CASCADE) 
    def __str__ (self):
        return nombre

################################## Proyecto Mensajes ############################################
# Andres
# 	Comunicados de un Conjunto cerrado 
class TipoMensaje (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Mensaje (models.Model):
    asunto          = models.CharField(max_length=200)
    fecha_creacion  = models.DateField(auto_now_add=True)
    contenido       = models.TextField(max_length=5000)
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    tipo            = models.ForeignKey(TipoMensaje, on_delete = models.CASCADE) 
    def __str__ (self):
        return asunto

################################## Proyecto Manualidades ############################################
# John Quimbaya
# 	Catalogo de Manualidades 

class Material (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Manualidad (models.Model):
    nombre          = models.CharField(max_length=200)
    descripcion     = models.TextField(max_length=5000)
    tiempo          = models.CharField(max_length=200)
    estado          = models.BooleanField(default=True)
    precio          = models.IntegerField(null=True, blank=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    material        = models.ForeignKey(Material, on_delete = models.CASCADE) 
    def __str__ (self):
        return nombre

################################## Proyecto Libros ############################################
# Angel Castillo
# 	Libro  ----  Autor
class Autor (models.Model):
    nombre          = models.CharField(max_length=200)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)

    def __str__ (self):
        return nombre

class Libro (models.Model):
    nombre          = models.CharField(max_length=200)
    descripcion     = models.TextField(max_length=5000)
    estado          = models.BooleanField(default=True)
    precio          = models.IntegerField(null=True, blank=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    autor           = models.ForeignKey(Autor, on_delete = models.CASCADE) 
    def __str__ (self):
        return nombre

################################## Proyecto Modulares Muebles ############################################
# Cristian Urbano
# 	Muebles modulares Hogar, Empresa

class TipoModular (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Modular (models.Model):
    nombre          = models.CharField(max_length=200)
    dimensiones     = models.TextField(max_length=50)
    estado          = models.BooleanField(default=True)
    precio          = models.IntegerField(null=True, blank=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    categoria       = models.ForeignKey(TipoModular, on_delete = models.CASCADE) 
    def __str__ (self):
        return nombre

################################## Proyecto Vehiculos ############################################
# Juan Pablo
# 	Vehiculos y sus respectivos tipos 
# 	Vehiculo  -----   Tipo 
# 		*				1	

class tipoVehiculo (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Vehiculo (models.Model):
    referencia      = models.CharField(max_length=200)
    marca           = models.CharField(max_length=200, null=True, blank=True)
    modelo          = models.CharField(max_length=200, null=True, blank=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    estado          = models.BooleanField(default=True)
    tipo            = models.ForeignKey(tipoVehiculo, on_delete = models.CASCADE) 
    def __str__ (self):
        return referencia

################################## Proyecto Tramites ############################################
# Santiago Pasaje
# 	Tramite -------  Tipo (carro/moto  , usuario)
# 		*				1
class tipoTramite (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Tramite (models.Model):
    nombre          = models.CharField(max_length=200)
    precio_auto     = models.IntegerField( null=True, blank=True)
    precio_moto     = models.IntegerField( null=True, blank=True)
    precio_usuario  = models.IntegerField( null=True, blank=True)
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    tipo            = models.ForeignKey(tipoTramite, on_delete = models.CASCADE) 
    def __str__ (self):
        return nombre

################################## Proyecto Consecionario ############################################
# Cristian Silva
# 	Ventas de vehiculos de un consecionario

# 	Cliente --- Venta --- Coche
class Propietario (models.Model):
    nombres         = models.CharField(max_length=200)
    correo          = models.EmailField(null=True, blank=True)
    telefono        = models.CharField(max_length=200, null=True, blank=True)
    direccion       = models.CharField(max_length=200, null=True, blank=True)


    def __str__ (self):
        return nombres

class Carro (models.Model):
    referencia      = models.CharField(max_length=200)
    marca           = models.CharField(max_length=200, null=True, blank=True)
    modelo          = models.IntegerField(null=True, blank=True)
    placa           = models.CharField(max_length=200, null=True, blank=True)
    precio          = models.IntegerField(null=True, blank=True)
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    propietario     = models.ForeignKey(Propietario, on_delete = models.CASCADE) 
    def __str__ (self):
        return referencia


################################## Proyecto Motos ############################################
# Israel Gomez
# 	Catalogo de Motos con su respectiva marca
# 	Moto  ----  Marca
# 	*            1
class Marca (models.Model):
    nombre         = models.CharField(max_length=200)
    pais_origen    = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Motocicleta (models.Model):
    referencia      = models.CharField(max_length=200)
    modelo          = models.IntegerField(null=True, blank=True)
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    marca           = models.ForeignKey(Marca, on_delete = models.CASCADE) 
    def __str__ (self):
        return referencia

################################## Proyecto Documentos ############################################
# Andres Reyes
# 	documentacion  y el tipo de documentacion 
# 	Documento  -----   tipo  (implementacion, optimizacion, ...)	
# 		*				1	
class TipoDocumento (models.Model):
    nombre         = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Documento (models.Model):
    fecha_elaboracion  = models.DateField(auto_now_add=True)
    descripcion     = models.TextField(max_length=5000)
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    tipo            = models.ForeignKey(TipoDocumento, on_delete = models.CASCADE) 
    
    def __str__ (self):
        return referencia

################################## Proyecto ensaladas Vegetales ############################################
# Doris
# 	comidas ensaladas vegetales,
# 	Comida 			---   	tipo
# 		*					1	
class TipoComida (models.Model):
    nombre          = models.CharField(max_length=200)

    def __str__ (self):
        return nombre

class Comida (models.Model):
    nombre          = models.CharField(max_length=200)
    ingredientes    = models.TextField(max_length=2000)
    precio          = models.IntegerField(null = True , blank = True)
    estado          = models.BooleanField(default=True)
    photo           = models.ImageField(upload_to = 'projects', null = True , blank = True)
    tipoComida       = models.ForeignKey(TipoComida, on_delete = models.CASCADE) 
    def __str__ (self):
        return nombre

################################## Fin ############################################

