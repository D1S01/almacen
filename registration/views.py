from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from ventasinventario.forms import administradorForm, jefeBodegaForm
from ventasinventario.models import Administrador, JefeBodega


# Create your views here.

class RegistrarseView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    def get_form(self, form_class = None):
        form = super().get_form()
              
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        
        
        return form
    
class PerfilView(UpdateView):
    model = Administrador or JefeBodega
    form_class = administradorForm or jefeBodegaForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')    
    
    def get_object(self):
        profile, created = JefeBodega.objects.get_or_create(user = self.request.user)
        return profile
      
    def get_object(self):
        profile, created = Administrador.objects.get_or_create(user = self.request.user)
        return profile
    
    