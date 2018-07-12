from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Paste


import uuid

def index(request):
    return HttpResponse("Hello, world. You're at the pastes index.")

def root(request):
	template = loader.get_template('paster/root.html')
	context = {

	}
	return HttpResponse(template.render(context, request))

def paste(request):
	# return HttpResponse("This should be some code here that will show a paste ")
    if request.POST['name'] == '' or request.POST['name'] == None:
        if request.POST['content'] == '' or request.POST['content'] == None:
            error_message = 'Name and content cannot be blank'
        else:
            error_message = 'Name cannot be blank'
        return render(request, 'paster/root.html', { 'error_message': error_message })
    elif request.POST['content'] == '' or request.POST['content'] == None:
        error_message = 'Content cannot be blank'
        return render(request, 'paster/root.html', { 'error_message': error_message })

    paste = Paste(paste_name=request.POST['name'],paste_content = request.POST['content'], date_of_expiry=request.POST['date_of_expiry'])
    rand_string = str(uuid.uuid4())[:10]
    while Paste.objects.filter(paste_url=rand_string):
        rand_string = str(uuid.uuid4())[:10]
    paste.paste_url = rand_string
    paste.save()
    # return HttpResponseRedirect(reverse('show', args=(paste.paste_url)))
    return HttpResponseRedirect(reverse('paster:show', args=(paste.paste_url,)))

def show(request,rand_string):
    paste = get_object_or_404(Paste, paste_url=rand_string)
    return render(request, 'paster/show.html', {'paste': paste})

def delete(request,rand_string):
    paste = get_object_or_404(Paste, paste_url=rand_string)
    paste.delete()
    return HttpResponseRedirect(reverse('paster:root'))

def search(request):
	inp = request.GET['nama']
	if inp =='':
		pastes = Paste.objects.all()
	else:
		pastes = Paste.objects.filter(paste_name = inp)
	return render(request, 'paster/search.html',{'pastes': pastes})

