from django.urls import path, re_path

from gui.views.main import rss, collapse
from gui.views.auth import authent, log_out
from gui.views import dashboard

urlpatterns = [
    path('login/', authent, name="gui.login"),
    path('logout/', log_out, name="gui.logout"),
    path('collapse', collapse, name="gui.collapse_menu"),

    re_path(r'^$', dashboard.dashboard_services, name="gui.dashboard.services"),
    path('rss/', rss, name='gui.rss'),
]