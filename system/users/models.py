
# Django system imports
from django.contrib.auth import models as auth_models
from djongo import models

# Django project imports
#from authentication.ldap.models import LDAPRepository

# Required exceptions imports

# Extern modules imports

# Logger configuration imports
import logging
logger = logging.getLogger('gui')


class User(auth_models.User):
    """
    Override of Django Users to add ldap_user attribute
    """
    is_ldapuser = models.BooleanField(default=False)

    class Meta:
        app_label = "system"
