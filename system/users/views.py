from django.http import JsonResponse, HttpResponseRedirect
from system.users.models import User
from gui.forms.form_utils import DivErrorList
from system.users.form import UserForm, UserLDAPForm
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
import json


def users_list(request):
    if not request.is_ajax():
        return render(request, "system/users.html")

    order = {
        "asc": "",
        "desc": "-"
    }

    start = int(request.POST['iDisplayStart'])
    length = int(request.POST['iDisplayLength']) + start

    search = request.POST['sSearch']
    columns = json.loads(request.POST['columns'])
    col_sort = columns[int(request.POST["iSortingCols"])]

    col_order = "{}{}".format(order[request.POST['sSortDir_0']], col_sort)

    s = Q()
    if search:
        s = Q(username__icontains=search)

    objs = []
    max_objs = User.objects.filter(s).count()
    for user in User.objects.filter(s).order_by(col_order)[start:length]:
        objs.append({
            'id': str(user.id),
            'groups': ", ".join([g.name for g in user.groups.all()]),
            'is_superuser': user.is_superuser,
            'username': user.username
        })

    return JsonResponse({
        "status": True,
        "iTotalRecords": max_objs,
        "iTotalDisplayRecords": max_objs,
        "aaData": objs
    })


def users_edit(request, object_id=None):
    """ Editing users view """
    if object_id:
        user = User.objects.get(pk=object_id)
    else:
        user = User()

    # Default User Form
    user_form = UserForm(request.POST or None, instance=user)
    # Default User template
    template = 'system/users_edit.html'

    # If User has been inserted from LDAP, specific form and template (no password edition)
    if user.is_ldapuser:
        user_form = UserLDAPForm(request.POST or None, instance=user)
        template = 'system/users_ldap_edit.html'

    if request.method == "GET" or not user_form.is_valid():
        return render(request, template, {
            'user_form': user_form
        })

    user.username = user_form.cleaned_data.get('username')
    user.is_superuser = user_form.cleaned_data.get('is_superuser')
    user.save()

    if user_form.cleaned_data.get('password1'):
        user.set_password(user_form.cleaned_data.get('password1'))

    groups = user_form.cleaned_data.get('groups')
    user.groups.set(groups)
    user.save()

    return HttpResponseRedirect(reverse('system.users.list'))
