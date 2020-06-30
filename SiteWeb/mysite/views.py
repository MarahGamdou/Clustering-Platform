from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context,request))

def kMeans(request):
	template = loader.get_template('kMeans.html')
	context = {}
	return HttpResponse(template.render(context,request))

def regroupementHierarchique(request):
	template = loader.get_template('regroupementHierarchique.html')
	context = {}
	return HttpResponse(template.render(context,request))

def dbscan(request):
	template = loader.get_template('dbscan.html')
	context = {}
	return HttpResponse(template.render(context,request))
