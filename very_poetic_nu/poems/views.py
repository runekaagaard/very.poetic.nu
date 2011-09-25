from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from very_poetic_nu.poems.models import Poem
from itertools import groupby
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	poems = Poem.objects.select_related().order_by('author__id').all()
	return render_to_response("poems/templates/index.html", {
		'poems': Poem.objects.select_related().order_by('author__id').all()})

def poem(request, pk):
	pk = int(pk)
	poem = get_object_or_404(Poem, pk=pk)
	try:
		poem_to_left = Poem.objects.get(pk=pk-1) 
	except ObjectDoesNotExist:
		poem_to_left=None
	try:
		poem_to_right = Poem.objects.get(pk=pk+1)
	except ObjectDoesNotExist:
		poem_to_right=None
	
	return render_to_response("poems/templates/poem.html", {
		'poem': poem,
		'poem_to_left': poem_to_left,
		'poem_to_right': poem_to_right,
	})

def random(request):
	return HttpResponseRedirect(Poem.objects.order_by('?')[0].id)