from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from system.system import System

import logging
logging.config.dictConfig(settings.LOG_SETTINGS)
logger = logging.getLogger('gui')


def admin_media(request):
    """ Middleware for Jinja template

    Args:
        request (Django request)

    Returns:
        DICT: Variable for jinja template
    """

    node_name = "OSS"

  

    menu = (System().menu)
    results = {
        'MENUS': menu,
        'VERSION': "OSS0.0.1",
        'CURRENT_NODE': node_name,
        'DEV_MODE': False,
        'TITLE': "OSS",
        'COLLAPSE': request.session.get('collapse')
    }
    print(results)
    return results
