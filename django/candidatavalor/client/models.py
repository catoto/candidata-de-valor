from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Evaluate(models.Model):
    text = models.TextField(max_length=500, verbose_name='nome')
    created_at = models.DateTimeField(u'criado em', default=timezone.now, editable=False)
    updated_at = models.DateTimeField(u'atualizado em', auto_now=True)
    is_active = models.BooleanField(u'ativo', default=True)

    class Meta:
        verbose_name = u'opção de avaliação'
        verbose_name_plural = u'opção de avaliações'
    
    def __str__(self):
        return "{}...".format(self.text[:50]) 


class PoliticalParty(models.Model):
    initials = models.CharField(max_length=128, verbose_name='sigla')
    name = models.CharField(max_length=128, verbose_name='nome')
    number = models.IntegerField(verbose_name='numero')

    class Meta:
        verbose_name = 'partido político'
        verbose_name_plural = 'partidos políticos'

    def __str__(self):
        return self.name


class Client(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(db_column='nome', verbose_name='nome', max_length=100)
    email = models.CharField(max_length=100, verbose_name='email')
    cargo = models.CharField(max_length=100, verbose_name='cargo')
    political_party = models.ForeignKey('PoliticalParty', verbose_name='partido')
    number = models.CharField(max_length=100, verbose_name='número')    
    image = models.ImageField(u'imagem detalhe', upload_to='event')
    proposal = models.CharField(max_length=100, verbose_name='proposta')
    created_at = models.DateTimeField(u'criado em', default=timezone.now, editable=False)
    updated_at = models.DateTimeField(u'atualizado em', auto_now=True)
    is_active = models.BooleanField(u'ativo', default=True)

    class Meta:
        verbose_name = 'candidato'
        verbose_name_plural = 'candidatos'

    def __str__(self):
        return self.name

# class proposal(models.Model)