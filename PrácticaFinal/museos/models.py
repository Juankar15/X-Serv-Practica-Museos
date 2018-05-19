from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Museo(models.Model):
	idmuseo = models.IntegerField()
	nombre = models.CharField(max_length = 32)
	descripcion_entidad = models.TextField()
	horario = models.TextField()
	transporte = models.TextField()
	accesibilidad = models.IntegerField(choices = ((0, '0'), (1, '1')))
	content_URL = models.URLField(max_length = 300)
	nombre_via = models.CharField(max_length = 64)
	clase_via = models.CharField(max_length = 64)
	tipo_num = models.CharField(max_length = 64)
	numero = models.CharField(max_length = 64)
	localidad = models.CharField(max_length = 64)
	provincia = models.CharField(max_length = 64)
	codigo_postal = models.TextField()
	barrio = models.CharField(max_length = 64)
	distrito = models.CharField(max_length = 64)
	coordenada_x = models.PositiveIntegerField()
	coordenada_y = models.PositiveIntegerField()
	latitud = models.FloatField(null = True, blank = True)
	longitud = models.FloatField(null = True, blank = True) 
	telefono = models.TextField()
	fax = models.TextField()
	email = models.TextField()
	tipo = models.TextField()
	
	
class Comentario(models.Model):
	museo = models.ForeignKey(Museo)
	texto = models.TextField()

class Escogido(models.Model):
	museo = models.ForeignKey(Museo)
	usuario = models.CharField(max_length = 32)
	fecha = models.DateField(auto_now = True)

class Estilo(models.Model):
	usuario = models.CharField(max_length = 32)
	letra = models.CharField(max_length = 64, null = True, blank = True)
	color = models.CharField(max_length = 32)
	titulo = models.CharField(max_length = 64, default = '')
