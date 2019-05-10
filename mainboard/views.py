from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from mainboard.models import Site, Item

def index(request):
    template = loader.get_template('mainboard/index.html')

    sites = Site.objects.all()
    context = {
        'sites': sites,
    }

    return HttpResponse(template.render(context, request))


def add(request):
    if request.method == 'GET':
        template = loader.get_template('mainboard/add.html')

        items = Item.objects.all()

        context = {
            'items': items,
        }

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponseRedirect(reverse('index', args=()))