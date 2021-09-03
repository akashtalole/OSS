from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

import logging.config
logging.config.dictConfig(settings.LOG_SETTINGS)
logger = logging.getLogger('gui')

def authent(request):
    """
    """
    error = None
    #url_next = request.GET.get('next', reverse('/'))
 
    def render_form(**kwargs):
        return render(request, 'logon.html', {
            #'url_next': url_next,
            **kwargs
        })

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            url_next = request.POST.get('next', '/')
            if url_next == "":
                url_next = "/"

            logger.info("User {} successfully authenticated".format(user.username))
            return HttpResponseRedirect(url_next)

        error = _("Failed to authenticate")
        logger.error('User {} failed to authenticate'.format(username))

    return render_form(error=error)

@login_required
def log_out(request):
    """
    """
    logout(request)
    return HttpResponseRedirect(reverse('gui.login'))
