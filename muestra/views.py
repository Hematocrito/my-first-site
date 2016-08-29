# Create your views here.
from django.shortcuts import render, render_to_response
from .forms import Formulario, FormularioContacto
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template import RequestContext


def mostrarTexto(request):
    return render_to_response("mipagina.html")


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

    return render_to_response('contacto_mail.html', {'formulario': formulario},
                                context_instance=RequestContext(request))


def profile(request):
    return render_to_response("intro.html")


def contacto(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
    return render(request, 'contacto.html', {
        'form': form,
        })
