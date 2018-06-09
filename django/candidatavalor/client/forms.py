# coding: utf-8
from django import forms
from client.models import PoliticalParty


default_error_messages = {
    'max_length': u'máximo de %(limit_value)d caracteres.',
    'min_length': u'mínimo de %(limit_value)d caracteres.',
}

class LoginForm(forms.Form):
    username = forms.EmailField(
        label=u'Email',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'SEU E-MAIL', 'type': 'text'}),
    )
    password = forms.CharField(
        label=u'Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'SUA SENHA'}),
        min_length=6,
        max_length=20,
        error_messages=default_error_messages,
    )


class ClientForm(forms.Form):

    name = forms.CharField(
        label=u'Nome',
        widget=forms.TextInput(attrs={'placeholder': 'SEU NOME'}),
        max_length=50,
    )
    email = forms.EmailField(
        label=u'Email',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'SEU E-MAIL', 'type': 'text'}),
    )
    password = forms.CharField(
        label=u'Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'SUA SENHA'}),
        min_length=6,
        max_length=20,
        error_messages=default_error_messages,
    )
    # check_password = forms.CharField(
    #     label=u'Confirmar senha',
    #     widget=forms.PasswordInput(attrs={'placeholder': 'SUA SENHA'}),
    #     min_length=6,
    #     max_length=20,
    #     error_messages=default_error_messages,
    # )
    cargo = forms.CharField(
        label=u'Cargo',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'SEU E-MAIL', 'type': 'text'}),
    )
    political_party = forms.IntegerField(
        label=u'Partido',
        widget=forms.Select(
            choices=PoliticalParty.objects.all().values_list('id', 'name')
        )
    )
    numero = forms.CharField(
        label=u'Número',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'SEU E-MAIL', 'type': 'text'}),
    ) 
    proposal = forms.CharField(
        label=u'Proposta',
        widget=forms.TextInput(attrs={'placeholder': 'SEU NOME'}),
        max_length=50,
    )

    # def clean_check_password(self):
    #     cd = super(ClientForm, self).clean()
    #     if not cd.get('password') == cd.get('check_password'):
    #         raise forms.ValidationError(u"As senhas não são iguais.")
    #     return cd['check_password']

