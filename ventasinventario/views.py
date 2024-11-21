from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Producto, Venta, Administrador, JefeBodega
from django.urls import reverse_lazy
from .forms import productoForm, ventasForm, SearchForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@method_decorator(login_required, name='dispatch')  
class CrearProductoview(CreateView):
    model = Producto
    template_name = 'ventasinventario/crearProducto.html'
    success_url = reverse_lazy('home')
    form_class = productoForm
    

@method_decorator(login_required, name='dispatch')      
class ListaProductosView(ListView):
    model = Producto
    template_name = 'ventasinventario/listaProductos.html'
    context_object_name = 'lista'

@method_decorator(login_required, name='dispatch')  
class ModificarProductoView(UpdateView):
    model = Producto
    template_name = 'ventasinventario/modificarProducto.html'
    success_url = reverse_lazy('home')
    form_class = productoForm

@method_decorator(login_required, name='dispatch')         
class EliminarProductoView(DeleteView):
    model = Producto
    template_name = 'ventasinventario/eliminarProducto.html'
    context_object_name = 'lista'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')       
class ListaVentasView(ListView):
    model = Venta
    template_name = 'ventasinventario/historialVentas.html'
    context_object_name = 'historial'

    def get_queryset(self):
        return Venta.objects.filter(administrador= Administrador.objects.get(user=self.request.user))
    
@method_decorator(login_required, name='dispatch')    
class RealizarVentaView(CreateView):
    model = Venta
    template_name = 'ventasinventario/crearVenta.html'
    success_url = reverse_lazy('listaVenta')
    form_class = ventasForm
    
    def form_valid(self, form):   
        admin = Administrador.objects.get(user = self.request.user)     
        form.instance.administrador = admin
        self.object = form.save()
        return super().form_valid(form)
#Agregue este metodo aca por que no sabia si se puede agregar fuera de una "class", este metodo ayudara a buscar los productos que filtrara por nombre
def buscar_productos(request):
    form = SearchForm()
    resultados = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Producto.objects.filter(nombre__icontains=query)
            
    return render(request, 'ventasinventario/buscar_productos.html', {'form': form, 'resultados': resultados})