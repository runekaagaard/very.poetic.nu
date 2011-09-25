from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from very_poetic_nu.poems.models import Poem

def index(request):
	return render_to_response("poems/templates/index.html", 
	                          {'poems': Poem.objects.order_by('author__id').all()})
