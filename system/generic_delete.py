# Django system imports
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

# Django project imports
from system.users.models import User

# Required exceptions imports
from django.core.exceptions import ObjectDoesNotExist

# Logger configuration imports
import logging
logging.config.dictConfig(settings.LOG_SETTINGS)
logger = logging.getLogger('gui')


class DeleteView(View):
    template_name = 'generic_delete.html'
    menu_name = _("")
    obj = None
    redirect_url = ""
    delete_url = ""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, object_id, **kwargs):
        try:
            obj_inst = self.obj.objects.get(pk=object_id)
        except ObjectDoesNotExist:
            return HttpResponseForbidden('Injection detected.')

        return render(request, self.template_name, {
            'object_id': object_id,
            'menu_name': self.menu_name,
            'delete_url': self.delete_url,
            'redirect_url': self.redirect_url,
            'obj_inst': obj_inst
        })

    def post(self, request, object_id, **kwargs):
        confirm = request.POST.get('confirm')
        if confirm == 'yes':
            try:
                obj_inst = self.obj.objects.get(pk=object_id)
            except ObjectDoesNotExist:
                return HttpResponseForbidden('Injection detected.')
            obj_inst.delete()
        return HttpResponseRedirect(self.redirect_url)



class DeleteUser(DeleteView):
    """ Class dedicated to delete an User object with its id """
    menu_name = _("System -> Users -> Delete")
    obj = User
    redirect_url = '/system/users/'
    delete_url = '/system/users/delete/'

    # get and post methods from mother class
