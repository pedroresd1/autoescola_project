from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('fullname','cpf','endereco','cep','cidade','estado','telefone','email')
        labels = {
            'fullname': 'Nome Completo',
            'cpf':'CPF',
            'endereco':'Endereço (Rua/Avenida)',
            'cep':'CEP',
            'cidade':'Cidade',
            'estado':'Estado',
            'telefone':'Telefone',
            'email':'Email'
        }