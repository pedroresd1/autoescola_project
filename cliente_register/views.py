from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

def cliente_list(request):
    context = {'cliente_list':Cliente.objects.all()}
    return render(request, "cliente_register/cliente_list.html", context)

def cliente_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = ClienteForm()
        else:
            cliente = Cliente.objects.get(pk=id)
            form = ClienteForm(instance=cliente)
        return render(request, "cliente_register/cliente_form.html", {'form':form}) 
    else:
        if id == 0:
            form = ClienteForm(request.POST)
        else: 
            cliente = Cliente.objects.get(pk=id)
            form = ClienteForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('/cliente/list')

def cliente_delete(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect('/cliente/list')