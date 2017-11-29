from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime
from .models import Cuentacajas
import django
from django.shortcuts import render
import PIL
import PIL.Image
import io
from io import *
import numpy as np
from chartit import DataPool, Chart
from django.shortcuts import render_to_response
from chartit.charts import *
from django.db.models import Avg,Sum,Count




def Cajas_chart_view(request):
    DatoBase = Cuentacajas.objects.all()
    #Step 1: Create a DataPool with the data we want to retrieve.
    DatosCajas = \
    DataPool(
    series=
        [{  'options': {
            'source': Cuentacajas.objects.order_by('Fecha')},
            'terms': [
            'HoraAct',
            'cant']}
        ])
    #Step 2: Create the Chart object
    cht = Chart(
    datasource = DatosCajas,
    series_options = [{'options':
                             {'type': 'line',
                              'stacking': False},
                              'terms':{'HoraAct': ['cant']}}],
    chart_options =   {'title': {'text': 'Cajas x Hora'},
                       'subtitle': {'text': 'El Subtitulo de mi grafico '},
                       'xAxis': {'title': {'text': 'Hora'}}})
        #Step 3: Send the chart object to the template.
    return render_to_response( 'monitoreoLinea/DisplayGraph.html', {'Cajas': cht,'DatoBase':DatoBase})


def Miconsulta(request):
    Misdatos = Cuentacajas.objects.filter(Hora='17')
    return render_to_response('monitoreoLinea/post_list.html',{'Hora':Misdatos})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def post_list(request):
    posts = Cuentacajas.objects.all()
    return render(request, 'monitoreoLinea/post_list.html', {'Cuentacajas': posts})

def DisplayGraph(request):
    # Step 1: Create a PivotDataPool with the data we want to retrieve.
    ds = PivotDataPool(
        series=[
            {'options': {
                'source': Cuentacajas.objects.all(),
                'categories': ['HoraAct']},
                'terms': {
                    'TotSum': Sum('cant')
                }
            }
        ]
    )

    # Step 2: Create the PivotChart object
    pivcht = PivotChart(
        datasource=ds,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['TotSum']
            }
        ],
        chart_options =
        {'title': {
            'text': 'Numeros Totales'},
            'xAxis': {
                'title': {
                    'text': 'Suma'}}}
    )

    # Step 3: Send the PivotChart object to the template.
    return render_to_response('monitoreoLinea/Grafico2.html', {'Countcajas': pivcht})




# Prueba de Varios graficos en un mismo HTML

def Dos_Graficos(request):
    # Defino Gráfico 1
    DatosCajas1 = \
        DataPool(
            series=
            [{'options': {
                'source': Cuentacajas.objects.all()},
                'terms': [
                    'HoraAct',
                    'cant']}
            ])
    # Step 2: Create the Chart object
    cht1 = Chart(
        datasource=DatosCajas1,
        series_options=[{'options':
                             {'type': 'line',
                              'stacking': False},
                         'terms': {'HoraAct': ['cant']}}],
        chart_options={'title': {'text': 'Cajas x Hora'},
                       'subtitle': {'text': 'Grafico 2 '},
                       'xAxis': {'title': {'text': 'Hora'}}})
    #Defino Grafico 2

    ds1 = PivotDataPool(
        series=[
            {'options': {
                'source': Cuentacajas.objects.all(),
                'categories': ['Hora']},
                'terms': {
                    'TotSum': Sum('cant')
                }
            }
        ]
    )

    # Step 2: Create the PivotChart object
    pivcht1 = PivotChart(
        datasource=ds1,
        series_options=[
            {'options': {
                'type': 'column'},
                'terms': ['TotSum']
            }
        ],
        chart_options=
        {'title': {
            'text': 'Numeros Totales'},
            'xAxis': {
                'title': {
                    'text': 'Hora'}}}
    )

    return render_to_response('monitoreoLinea/MultiplesGraficoa.html', {'Lista_Graficos': [cht1,pivcht1]})

from django.shortcuts import render

def application(environ, start_response):
    start_response('200 OK',[('Content-type','text/html')])
    return ['<html><body>Hello World!</body></html>']

# Create your views here.
