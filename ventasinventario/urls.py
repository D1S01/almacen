"""almacen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from ventasinventario.views import ListaProductosView, CrearProductoview, ModificarProductoView, EliminarProductoView, ListaVentasView,  RealizarVentaView, buscar_productos

urlpatterns = [
    path('', ListaProductosView.as_view(), name= 'home'),
    path('crearProducto/', CrearProductoview.as_view(), name= 'crearProducto'),
    path('modificarProducto/<int:pk>/', ModificarProductoView.as_view(), name= 'modificarProducto'),
    path('eliminarProducto/<int:pk>/', EliminarProductoView.as_view(), name= 'eliminarProducto'),
    path('ventas/', RealizarVentaView.as_view(), name= 'ventas'),
    path('listaVenta/', ListaVentasView.as_view(), name= 'listaVenta'),
    path('crearVenta/', RealizarVentaView.as_view(), name= 'crearVenta'),
    path('buscar/', buscar_productos, name= 'buscar_productos'),
]
