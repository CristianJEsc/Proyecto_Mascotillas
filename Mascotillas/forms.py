from django import forms

class MascotasFormulario(forms.Form):
    animal=forms.CharField()
    raza=forms.CharField()
    nombre=forms.CharField()
    fecha_nacimiento = forms.DateField()
   
class ProductosFormulario(forms.Form):
    nombre=forms.CharField()
    marca=forms.CharField()
    precio= forms.IntegerField()
    

class ServiciosFormulario(forms.Form):
    nombre=forms.CharField()
    precio= forms.IntegerField()


