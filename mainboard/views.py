from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from mainboard.models import Site, Item

def index(request):
    template = loader.get_template('mainboard/index.html')

    context = {

    }

    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('mainboard/add.html')

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return HttpResponse(template.render(context, request))