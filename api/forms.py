from django import forms


class AutorForm(forms.Form):
    nombre = forms.CharField(widget={})
    apellidos = forms.CharField()
    email = forms.EmailField()

