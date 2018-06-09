from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^avaliar$',
        views.AvaliarView.as_view(),
        name='avaliar'),
    url(r'^cadastro$',
        views.SingupView.as_view(),
        name='singup'),
    url(r'^login$',
        views.LoginView.as_view(),
        name='login'),
    url(r'^logout$',
        views.LogoutView.as_view(),
        name='logout'),
        
)