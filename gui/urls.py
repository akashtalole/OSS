from django.urls import path, re_path

from gui.views.auth import authent, log_out


urlpatterns = [
    path('login/', authent, name="gui.login"),
    path('logout/', log_out, name="gui.logout"),
]