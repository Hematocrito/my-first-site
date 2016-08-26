# - *- coding: latin-1 - *-


from django.shortcuts import render_to_response
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.template import RequestContext


def inicio(request):
    return render_to_response("index.html")


def legal(request):
    return render_to_response("legal.html")


def abogados(request):
    return render_to_response("abogados.html")


def contactomail(request):
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            asunto = 'Este es un mensaje de mi pagina de CONTACTO'
            mensaje = formulario.cleaned_data['mensaje']
            correo = formulario.cleaned_data['correo']
            msg = 'Envía: ' + correo + ' \n\n' + mensaje
            mail = EmailMessage(asunto, msg, to=['aussonia@gmail.com'])
            mail.send()
            return HttpResponseRedirect('/')
    else:
        formulario = FormularioContacto()

    return render_to_response('contacto.html', {'formulario': formulario},
                                context_instance=RequestContext(request))