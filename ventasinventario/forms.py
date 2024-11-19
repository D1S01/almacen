from .models import Producto, Venta, Administrador, JefeBodega
from django import forms

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }
    
class ventasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['total', 'montoRecibido', 'producto']
        widgets = {
            'total': forms.NumberInput(attrs={'class':'form-control'}),
            'montoRecibido': forms.NumberInput(attrs={'class':'form-control'}),
            'producto': forms.SelectMultiple(attrs={'class':'form-control'}),
        }
        
class administradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'rol']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'rol': forms.TextInput(attrs={'class':'form-control'}),
        }
        
class jefeBodegaForm(forms.ModelForm):
    class Meta:
        model = JefeBodega
        fields = ['nombre', 'rol']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'rol': forms.TextInput(attrs={'class':'form-control'}),
        }

#clase para agregar el formulario de busqueda de productos

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)