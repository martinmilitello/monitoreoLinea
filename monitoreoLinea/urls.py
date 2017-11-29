"""monitoreoLinea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin

from django.conf.urls import url
from MonitoreoDatos import views
from MonitoreoDatos.views import current_datetime
from MonitoreoDatos.views import Miconsulta,DisplayGraph
from MonitoreoDatos.views import Cajas_chart_view
from MonitoreoDatos.views import hours_ahead



urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),

    url(r'^$', views.post_list, name='post_list'),
    # url(r'DisplayGraph^$', views.DisplayGraph, name='DisplayGraph'),
    url(r'^DisplayGraph/$', views.DisplayGraph, name='DisplayGraph'),
    url(r'^Cajas_chart_view/$', views.Cajas_chart_view, name='Cajas_chart_view'),
    url(r'^Dos_Graficos/$', views.Dos_Graficos, name='Dos_Graficos'),
    url(r'^admin/', admin.site.urls),
    url(r'^Cajas_chart_view/$',Cajas_chart_view),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^Miconsulta/$',Miconsulta),
    # url(r'^simple.png$', views.simple('simple.png'), name='simple'),
]
