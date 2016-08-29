# -*- coding: utf-8 -*-
from django import forms


class FormularioContacto(forms.Form):
    correo = forms.EmailField()
    mensaje = forms.CharField()


class Formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    mensaje = forms.CharField()
    mail = forms.EmailField()
