from django.shortcuts import render
from museos.models import Museo, Comentario, Escogido, Estilo
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def pagina_principal(peticion):
   
    if peticion.method == "POST":
        if "boton" in peticion.POST:
            eleccion = peticion.POST['boton']
           
           
        else:
            eleccion = ""
            
            # http://stackoverflow.com/questions/2792650/python3-error-import-error-no-module-name-urllib2
            ArchivoXML = urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full")
            tree = ET.parse(ArchivoXML)
            root = tree.getroot()

            for elemento in tree.iter():
                if "ID-ENTIDAD" in elemento.attrib.values():   # Es un diccionario
                    museo_nuevo = Museo(idmuseo = elemento.text)
                elif "NOMBRE" in elemento.attrib.values():
                    museo_nuevo.nombre = elemento.text
                elif "DESCRIPCION-ENTIDAD" in elemento.attrib.values():
                    museo_nuevo.descripcion_entidad = elemento.text
                elif "HORARIO" in elemento.attrib.values():
                    museo_nuevo.horario = elemento.text
                elif "TRANSPORTE" in elemento.attrib.values():
                    museo_nuevo.transporte = elemento.text
                elif "ACCESIBILIDAD" in elemento.attrib.values():
                    museo_nuevo.accesibilidad = elemento.text
                elif "CONTENT-URL" in elemento.attrib.values():
                    museo_nuevo.content_URL = elemento.text
                elif "NOMBRE-VIA" in elemento.attrib.values():
                    museo_nuevo.nombre_via = elemento.text
                elif "CLASE-VIAL" in elemento.attrib.values():
                    museo_nuevo.clase_via = elemento.text
                elif "TIPO-NUM" in elemento.attrib.values():
                    museo_nuevo.tipo_num = elemento.text
                elif "NUM" in elemento.attrib.values():
                    museo_nuevo.numero = elemento.text
                elif "LOCALIDAD" in elemento.attrib.values():
                    museo_nuevo.localidad = elemento.text
                elif "PROVINCIA" in elemento.attrib.values():
                    museo_nuevo.provincia = elemento.text
                elif "CODIGO-POSTAL" in elemento.attrib.values():
                    museo_nuevo.codigo_postal = elemento.text
                elif "BARRIO" in elemento.attrib.values():
                    museo_nuevo.barrio = elemento.text
                elif "DISTRITO" in elemento.attrib.values():
                    museo_nuevo.distrito = elemento.text
                elif "COORDENADA-X" in elemento.attrib.values():
                    museo_nuevo.coordenada_x = elemento.text
                elif "COORDENADA-Y" in elemento.attrib.values():
                    museo_nuevo.coordenada_y = elemento.text
                elif "LATITUD" in elemento.attrib.values():
                    museo_nuevo.latitud = elemento.text
                elif "LONGITUD" in elemento.attrib.values():
                    museo_nuevo.longitud = elemento.text
                elif "TELEFONO" in elemento.attrib.values():
                    museo_nuevo.telefono = elemento.text
                elif "FAX" in elemento.attrib.values():
                    museo_nuevo.fax = elemento.text
                elif "EMAIL" in elemento.attrib.values():
                    museo_nuevo.email = elemento.text
                elif "TIPO" in elemento.attrib.values():
                    museo_nuevo.save()
                else:
                    pass
  

    lista_museos = Museo.objects.all()
    if len(lista_museos) == 0: #Si no hay ningun museo los cargamos
        cargar = True
    else:
        cargar = False

    template = get_template('pagina_principal.html')
    context = RequestContext(peticion, {
                                        'cargar': cargar})

    resp = template.render(context)
    return HttpResponse(resp)
@csrf_exempt
def pagina_museos(peticion):
    lista_museos = ''
    distrito = ''
    if peticion.method == 'POST':
        if "opciones" in peticion.POST:
            distrito = peticion.POST['opciones']
            if distrito == "Todos":
                lista_museos = Museo.objects.all()
            else:
                lista_museos = Museo.objects.filter(distrito = distrito)

    if peticion.method == 'GET':
        museos = Museo.objects.all()
        distrito = "Todos"
    # Obtengo todos los valores de distrito
    ListaTodos_distritos = Museo.objects.all().values_list('distrito')
    # Obtengo los valores unicos de una lista
    # http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    ListaUnico_distrito = list(set(ListaTodos_distritos))
    # http://stackoverflow.com/questions/10941229/convert-list-of-tuples-to-list
    ListaUnico_distrito = [distrito[0] for distrito in ListaUnico_distrito]

    template = get_template('museos.html')
    context = RequestContext(peticion, {'ListaTodos_distritos': ListaUnico_distrito,
                                        'museos': lista_museos,
                                        'distrito': distrito,
                                        })
    return HttpResponse(template.render(context))
	
