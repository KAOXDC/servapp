from django.urls import path, include 
from rest_framework import routers 
from .views import *

router = routers.DefaultRouter()
# router.register(r'productos', producto_viewset)
# router.register(r'marca', marca_viewset)
# router.register(r'categoria', categoria_viewset)
router.register(r'obra', Obra_viewset)
router.register(r'elemento', Elemento_viewset)
router.register(r'elementoobra', ElementoObra_viewset)
router.register(r'enfermedad', Enfermedad_viewset)
router.register(r'medicamento', Medicamento_viewset)
router.register(r'categoria', Categoria_viewset)
router.register(r'producto', Producto_viewset)
router.register(r'tipomensaje', TipoMensaje_viewset)
router.register(r'mensaje', Mensaje_viewset)
router.register(r'material', Material_viewset)
router.register(r'manualidad', Manualidad_viewset)
router.register(r'autor', Autor_viewset)
router.register(r'libro', Libro_viewset)
router.register(r'tipomodular', TipoModular_viewset)
router.register(r'modular', Modular_viewset)
router.register(r'tipovehiculo', tipoVehiculo_viewset)
router.register(r'vehiculo', Vehiculo_viewset)
router.register(r'tipotramite', tipoTramite_viewset)
router.register(r'tramite', Tramite_viewset)
router.register(r'propietario', Propietario_viewset)
router.register(r'carro', Carro_viewset)
router.register(r'marca', Marca_viewset)
router.register(r'motocicleta', Motocicleta_viewset)
router.register(r'tipodocumento', TipoDocumento_viewset)
router.register(r'documento', Documento_viewset)
router.register(r'tipocomida', TipoComida_viewset)
router.register(r'comida', Comida_viewset)




urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
