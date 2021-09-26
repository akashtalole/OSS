from system.generic_delete import DeleteUser
from system.users import views
from django.urls import path

urlpatterns = [
    path('system/users/', views.users_list, name="system.users.list"),
    path('system/users/edit/', views.users_edit, name="system.users.edit"),
    path('system/users/edit/<int:object_id>', views.users_edit,
         name="system.users.edit"),
    path('system/users/delete/<int:object_id>', DeleteUser.as_view(),
         name="system.users.delete")
]
