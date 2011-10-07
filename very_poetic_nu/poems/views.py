# coding=utf-8
from itertools import groupby

from django.shortcuts import (get_object_or_404, render_to_response, 
                              RequestContext, redirect)
from django.http import (HttpResponse, HttpResponseRedirect, 
                         HttpResponseForbidden)
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from django import forms
from django.contrib.auth import logout as _logout

from very_poetic_nu.poems.models import Poem


def index(request):
	poems = Poem.objects.select_related().order_by(
		                                    'user__id').filter(deleted=False)
	return render_to_response("poems/index.html", {
		'poems': poems,
		'request': request,
	})

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
	
	poem.content = poem.content.replace(" ", "&nbsp;")
	return render_to_response("poems/poem.html", {
		'poem': poem,
		'poem_to_left': poem_to_left,
		'poem_to_right': poem_to_right,
		'request': request,
		'user_owns_poem': user_owns_poem(request, poem)
	})

def random(request):
	return HttpResponseRedirect(Poem.objects.order_by('?')[0].id)

class PoemForm(ModelForm):
	class Meta:
		model = Poem

def add(request):
	return edit(request, None)

def user_owns_poem(request, poem):
	return poem.user == request.user

def edit(request, pk):
	if pk is not None:
		poem = get_object_or_404(Poem, pk=int(pk))
		if not user_owns_poem(request, poem):
			return HttpResponseForbidden()
	else:
		poem = None
	
	if request.method == 'POST':
		form = PoemForm(request.POST, instance=poem)
		if pk is None:
			form.instance.user = request.user

		if form.is_valid():
			form.save()

			return redirect('poem', form.instance.pk)
	else:
		form = PoemForm(instance=poem)

	return render_to_response('poems/change.html', { 'form': form,}, 
	                          RequestContext(request))

def delete(request, pk):
	poem = get_object_or_404(Poem, pk=pk)
	if not user_owns_poem(request, poem):
			return HttpResponseForbidden()

	if request.method == 'POST':
		if 'confirm' in request.POST:
			poem.deleted = True
			poem.save()

		return redirect('index')

	return render_to_response('poems/delete.html', {}, 
	                          RequestContext(request))

def restore(request, pk):
	poem = get_object_or_404(Poem, pk=pk)
	if not user_owns_poem(request, poem):
			return HttpResponseForbidden()

	if request.method == 'POST':
		if 'confirm' in request.POST:
			poem.deleted = False
			poem.save()

		return redirect('index')

	return render_to_response('poems/restore.html', {}, 
	                          RequestContext(request))

def logout(request):
  _logout(request)
  return redirect('index')