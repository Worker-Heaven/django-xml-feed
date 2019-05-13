from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from mainboard.models import Site, Item, Config


def index(request):
    template = loader.get_template('mainboard/index.html')

    config = Config.objects.all()
    context = {
        'config': config,
    }

    return HttpResponse(template.render(context, request))


def sites_new(request):
    if request.method == 'GET':
        template = loader.get_template('mainboard/sites_new.html')

        items = Item.objects.all()

        context = {
            'items': items,
        }

        return HttpResponse(template.render(context, request))

    else:
        selected_items = request.POST.getlist('items-list')
        url = request.POST.get('site-url')

        if len(selected_items) > 0 and len(url) > 0:
            # NOTE: Add new site info
            new_site = Site()
            new_site.url = url

            new_site.save()

            for item in selected_items:
                new_site.items.add(
                    Item.objects.get(label=item)
                )


            return HttpResponseRedirect(
                reverse(
                    'sites_config_new',
                    kwargs={'site_id': new_site.id},
                    )
                )

        else:
            return HttpResponseRedirect(reverse('sites_new'))


def sites_details(request, site_id):
    config = Config.objects.get(site=Site.objects.get(id=site_id))

    return HttpResponse('You are on the details page of {}'.format(site_id))


def sites_config_new(request, site_id):
    if request.method == 'GET':
        template = loader.get_template('mainboard/sites_config_new.html')

        site = Site.objects.get(id=site_id)
        context = {
            'items': site.items.all(),
            'site_id': site_id,
            }

        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        period = request.POST.get('scraping-period')
        selected_items = request.POST.getlist('items-list')

        if len(selected_items) > 0:
            config = Config()
            config.period = period
            config.site = Site.objects.get(id=site_id)
            config.save()

            for item in selected_items:
                config.items.add(Item.objects.get(label=item))

            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(
                reverse(
                    'sites_config_new',
                    kwargs={'site_id': site_id},
                )
            )
    return HttpResponse('You are on the config ')


def sites_config_details(request, site_id, config_id):
    template = loader.get_template('mainboard/sites_config_details.html')

    config = Config.objects.get(id=config_id)

    context = {
        'items': config.items.all(),
        }

    return HttpResponse(template.render(context, request))
