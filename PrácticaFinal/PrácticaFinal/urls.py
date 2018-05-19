"""PrácticaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from museos import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^css$', views.css),
    url(r'^templates/styles\.css', views.css),
    url(r'museos/templates/styles\.css$', views.css),
    url(r'^about$', views.about, name = "Página autoría de la práctica y funcionamiento"),
    url(r'^$', views.pagina_principal, name = "Página principal de la práctica"),
    url(r'^cambiar_titulo', views.cambiar_titulo),
    url(r'^login/?$', views.login, name = "Login de usuarios"),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^museos$', views.pagina_museos, name = "Página con todos los museos"),
    url(r'^museos/(\d+)', views.pagina_museo, name = "Página de un museo"), 
     url(r'^(.*)/xml$', views.pagina_xml, name = "Canal XML"),
    url(r'^(.*)$', views.pagina_usuario, name = "Página personal de un usuario"),
    
]
