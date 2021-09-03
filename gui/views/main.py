from django.http import JsonResponse
from django.conf import settings
import logging.config
import json

logging.config.dictConfig(settings.LOG_SETTINGS)
logger = logging.getLogger('gui')

def rss(request):
    """
        Fetch all not acknowledged RSS informations
        ordered by date
    """
    if request.method == "GET":
        #rss = [r.to_template() for r in
        #       RSS.objects.filter(ack=False).order_by('-date')]

        return JsonResponse({
            'status': True,
            'rss': "test"
        })

    # If POST, acknowledge the RSS
    rss_id = request.POST['rss']

    return JsonResponse({
        'status': True
    })

def collapse(request):
    request.session['collapse'] = request.GET['collapse'] == "true"

    return JsonResponse({
        'status': True
    })
