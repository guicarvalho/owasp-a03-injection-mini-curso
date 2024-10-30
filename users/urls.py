from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.list_users, name="list_users"),
    path("create/", views.create_user, name="create_user"),
]
