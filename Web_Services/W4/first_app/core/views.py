from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader


def index(request):
    return HttpResponse('ok')


def my_view(request):
    # t = loader.get_template('myapp/index.html')
    # context = {'foo': 'bar'}
    # return HttpResponse(t.render(context, request))
    return render(request, 'myapp/index.html', {'foo': 'bar'})


def my_view_redirect(request):
    return redirect('/some/url')
