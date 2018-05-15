from django.shortcuts import render
from museos.models import Museo, Comentario, Escogido, Estilo
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Count
from django.template import Context
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.core.exceptions import ObjectDoesNotExist
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
        else:
            if "marcar" in peticion.POST:
                recibido = peticion.POST['marcar']
                idmuseo = recibido.split(',')[0]
                nombre_usuario = recibido.split(',')[1]
                museo = Museo.objects.get(idmuseo = idmuseo)
                usuario = User.objects.get(username = nombre_usuario)
                fecha = timezone.now()
                NueElec = Escogido(museo = museo, usuario = usuario, fecha = fecha)
                NueElec.save()
            else:
                recibido = peticion.POST['desmarcar']
                idmuseo = recibido.split(',')[0]
                nombre_usuario = recibido.split(',')[1]
                museo = Museo.objects.get(idmuseo = idmuseo)
                usuario = User.objects.get(username = nombre_usuario)
                BorrarElec = Escogido.objects.get(museo = museo, usuario = usuario)
                BorrarElec.delete()

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

    if peticion.user.is_authenticated():
        Escogidos = Escogido.objects.all().values_list('museo').filter(usuario = peticion.user)
        lista_Escogidos = [Escogido[0] for Escogido in Escogidos]
    else:
        lista_Escogidos = ""

    template = get_template('museos.html')
    context = RequestContext(peticion, {'ListaTodos_distritos': ListaUnico_distrito,
                                        'museos': lista_museos,
                                        'distrito': distrito,
                                        'Escogidos': lista_Escogidos})
                                        
    return HttpResponse(template.render(context))

@csrf_exempt
def login(peticion):
    if peticion.method =="POST":
        username = peticion.POST['username']
        password = peticion.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(peticion, user)
        return HttpResponseRedirect('/')
    else:
        template = get_template('error.html')
        return HttpResponse(template.render(Context({'texto': "Usuario no autenticado"})))
@csrf_exempt
def logout(peticion):
    if peticion.method == "POST":
        logout(peticion)
    return HttpResponseRedirect('/')
        
def pagina_usuario(peticion, usuario_):
    if peticion.method == "GET":
        try:
            usuario = User.objects.get(username = usuario_)
        except User.DoesNotExist:
            template = get_template('error.html')
            return HttpResponse(template.render(), status=404)
        # Obtener una query string:
        # https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.META
        query_string = peticion.META['QUERY_STRING']
   
    else:
        query_string = ""
        if peticion.user.is_authenticated():
            usuario = User.objects.get(username = peticion.user.username)
            try:
                usuario = Estilo.objects.get(usuario = usuario)
            except:
                user = User.objects.get(username = peticion.user.username)
                usuario = Estilo(usuario = user)

            if 'titulo' in peticion.POST:
                usuario.titulo = peticion.POST['titulo']
            else:
                usuario.letra = peticion.POST['letra']
                usuario.color = peticion.POST['color']
            usuario.save()

    template = get_template('pagina_usuario.html')
    usuario = User.objects.get(username = usuario_)
    if query_string == "":
        Escogidos = Escogido.objects.filter(usuario = usuario)
    else:
        restantes = Escogido.objects.filter(id__gt = (int(query_string)))
        Escogidos = restantes.filter(usuario = usuario)

    if len(Escogidos) <= 5:
        fin = True
    else:
        fin = False

    try:
        usuario = Estilo.objects.get(usuario = usuario)
    except:
        usuario = ""

    context = RequestContext(peticion, {'usuario': usuario,
                                        'usuario_': usuario_,
                                        'Escogidos': Escogidos,
                                        'fin': fin})
    resp = template.render(context)
    return HttpResponse(resp)
    
@csrf_exempt   
def cambiar_titulo(peticion):
	
    if peticion.method == "POST":
        titulo = peticion.POST['titulo']
        try:
            cambio = Estilo.objects.get(usuario = peticion.user.username)
            cambio.titulo = titulo
            cambio.save()
        except:
            cambio = Estilo(usuario = peticion.user.username, titulo = titulo)
            cambio.save()
        direccion = '/' + peticion.user.username
        return HttpResponseRedirect(direccion)  
         
def about(peticion):
    template = get_template('about.html')
    context = RequestContext(peticion)
    return HttpResponse(template.render(context))
