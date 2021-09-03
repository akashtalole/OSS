from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import logging.config

logging.config.dictConfig(settings.LOG_SETTINGS)
logger = logging.getLogger('debug')


def dashboard_services(request):
    if request.is_ajax():
             return JsonResponse({
                'monitor': {"gui": "True"},
                'status': True
            })

        
            
    #return JsonResponse({'status': False})

    return render(request, 'dashboard_services.html', {
        'nodes': {"node1":"1"}
    })
