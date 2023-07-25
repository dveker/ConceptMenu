from django.template import loader
from django.http import HttpResponse

def members(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())

def abotpaje(request):
  template = loader.get_template('abotpaje.html')
  return HttpResponse(template.render())