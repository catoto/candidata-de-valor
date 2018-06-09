from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.views.generic import View
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect

from client.forms import ClientForm, LoginForm
from client.models import Client, Evaluate, PoliticalParty

import logging


logger = logging.getLogger('candidata-valor')


class BaseView(View):

    @property
    def client(self):
        try:
            client = self.request.session.get('client')
            return client
        except:
            return None


class AvaliarView(BaseView):

    def __init__(self):
        self._template = 'avaliar.html'
    
    def get_context(self):
        context = {
            'client': self.client,
            'evaluete': Evaluate.objects.filter(is_active=True), 
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self._template, context)


class HomeView(BaseView):

    def __init__(self):
        self._template = 'home.html'
    
    def get_context(self):
        context = {
            'client': self.client
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self._template, context)


class LoginView(BaseView):

    def __init__(self):
        self._template = 'login.html'

    def get_context(self):
        form = LoginForm()
        context = {
            'form': form,
            'client': self.client
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self._template, context)
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                client = Client.objects.get(user=user)
                request.session['client'] = client
                logger.info(
                    u'Client: {} loged in successfully'.format(client))
                return HttpResponseRedirect('/')
                logger.info(u'Client: {} fail to loged in, user is inactive'.format(client))
                messages.error(request, u'Usuário inativo')
            except Exception:
                logger.error(u'Loged in attempt fail for user: {} user is inactive.'.format(username))
                messages.error(request, u'Usuário inválido')
        else:
            logger.error(u'Loged in attempt fail for user: {}'.format(username))
            # Return an 'invalid login' error message.
            messages.error(request, u'Usuário inválido')

        return HttpResponseRedirect('/')


class SingupView(BaseView):

    def __init__(self):
        self._template = 'cadastro.html'

    def get_context(self):
        form = ClientForm()
        context = {
            'form': form,
            'client': self.client
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self._template, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        logger.debug('SINGUP POST - BODY')
        logger.debug(request.body)
        form = ClientForm(request.POST)
        context.update({
            'form': form
        })

        if not form.is_valid():
            logger.debug('SINGUP FORM INVALID')
            logger.debug(form.errors.as_text)
            context.update({
                'is_singup': True
            })
            return render(request, self._template, context)

        logger.debug(u'SINGUP FORM VALID')
        logger.debug(u'name: {}'.format(form.data.get('name')))
        logger.debug(u'email: {}'.format(form.data.get('email')))
        logger.debug(u'cargo: {}'.format(form.data.get('cargo')))
        logger.debug(u'political_party: {}'.format(form.data.get('political_party')))
        logger.debug(u'proposal: {}'.format(form.data.get('proposal')))
        logger.debug(u'password: {}'.format(form.data.get('password')))
    
        # user
        password = form.data.get('password')
        email = form.data.get('email')
        # check
        has_user = User.objects.filter(username=email)
        if has_user:
            logger.info(u'Email: {} already exists'.format(email))
            context.update({
                'email_exist': True
            })
            return render(request, self._template, context)

        has_email = Client.objects.filter(email=email)
        if has_email:
            logger.info(u'Email: {} already exists'.format(email))
            context.update({
                'email_exist': True
            })
            return render(request, self._template, context)
        
        with transaction.atomic():
            user = User(username=email)
            user.set_password(password)
            user.save()
            # Get politicatl Party

            client = Client(
                user=user,
                name=form.data.get('name'),
                email=email,
                cargo=form.data.get('cargo'),
                political_party=PoliticalParty(id=form.data.get('political_party')),
                proposal=form.data.get('proposal'),
            )
            client.save()
            request.session['client'] = client

        return render(request, self._template, context)


class LogoutView(View):

    def get(self, request):
        try:
            logger.info(u'Client: {} loged out successfully'.format(request.session['client']))
        except Exception as e:
            logger.error('Fail to log logou action...', e)
        logout(request)
        request.user = None
        return HttpResponseRedirect("/")