from django.utils.translation import ugettext as _
from django.conf import settings

import logging
import logging.config

logging.config.dictConfig(settings.LOG_SETTINGS)

logger = logging.getLogger('system')


class System:

    def __init__(self):
        self.logger = logging.getLogger('system')

    @property
    def menu(self):
        MENU = {
            'link': 'system',
            'icon': 'fa fa-microchip',
            'text': _('System'),
            'url': "#",
            'submenu': [{
                'link': 'users',
                'text': 'Users',
                'url': '/system/users'
            }

            ]
        }

        return MENU
