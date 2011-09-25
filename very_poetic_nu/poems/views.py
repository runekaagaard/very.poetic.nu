from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from very_poetic_nu.poems.models import Poem
from itertools import groupby

def index(request):
	poems = Poem.objects.select_related().order_by('author__id').all()
	return render_to_response("poems/templates/index.html", {
		'poems': Poem.objects.select_related().order_by('author__id').all()})

def poem(request, id):
	poem = get_object_or_404(Poem, pk=id)
	return render_to_response("poems/templates/poem.html", {'poem': poem})