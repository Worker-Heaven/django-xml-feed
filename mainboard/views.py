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


def sites_new(request):
    if request.method == 'GET':
        template = loader.get_template('mainboard/add.html')

        items = Item.objects.all()

        context = {
            'items': items,
        }

        return HttpResponse(template.render(context, request))

    else:
        selected_items = request.POST.getlist('items-list')

        if len(selected_items) > 0:
            print(selected_items)

        return HttpResponseRedirect(reverse('index', args=()))


def sites_details(request, site_id):
    return HttpResponse('You are on the details page of {}'.format(site_id))


def sites_config_new(request, site_id):
    return HttpResponse('You are on the config ')


def sites_config_details(request, site_id, config_id):
    return HttpResponse('You are on the config details page {}, {}'.format(site_id, config_id))