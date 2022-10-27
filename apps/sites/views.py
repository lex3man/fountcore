from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from apps.sites.models import Site, Item

class GetItem(View):
    def get(self, request):
        host = request.GET.get("domain")
        domain = "www."+str(host).replace("www.","").replace("http://","").replace("/","")
        data = {'id':'None', 'host':host, 'domain':domain}
        try: 
            site = Site.objects.get(domain = domain)
            data.update({'id':site.pk, 'site':site.caption})
        except: data.update({'site':'None'})
        items = [data]
        items_query = Item.objects.filter(site = site)
        for item in items_query:
            data = {
                'id':item.identity,
                'caption':item.caption,
                'description':item.description
            }
            items.append(data)
        return JsonResponse(items, safe=False)