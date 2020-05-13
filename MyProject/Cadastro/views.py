from django.shortcuts import render,redirect
from .models import DataRegistro
from .forms import RegistroForm
from django.contrib import messages
# Create your views here.

def home(request):
    context = { }
    return render(request, "home.html", context)

def sobre_mapeamento(request):
    context = { }
    return render(request, "sobre_mapeamento.html", context)

def vertente_do_map(request):
    context = { }
    return render(request, "vertente_do_map.html", context)


def mapeamento_atual(request):
    context = { }
    return render(request, "mapeamento_atual.html", context)

def registro(request):
    context = { "form": RegistroForm }
    return render(request, "registro.html", context)

def addUsers(request):
    form = RegistroForm(request.POST)
    if form.is_valid():
        registro = DataRegistro(Empresa=form.cleaned_data['Empresa'],
                                Email=form.cleaned_data['Email'],
                                Site=form.cleaned_data['Site'],
                                Rua=form.cleaned_data['Rua'],
                                Bairro=form.cleaned_data['Bairro'],
                                Cidade=form.cleaned_data['Cidade'],
                                Estado=form.cleaned_data['Estado'],
                                CEP=form.cleaned_data['CEP'],
                                CNPJ=form.cleaned_data['CNPJ']
                                )
        registro.save()
        
        return redirect('add')


        










