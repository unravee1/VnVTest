from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('groups', views.groups),
    path('create_user', views.create_user),
    path('create_group', views.create_group),
    path("edit_user/<int:id>/", views.edit_user),
    path("delete_user/<int:id>/", views.delete_user),
    path("edit_group/<int:id>/", views.edit_group),
    path("delete_group/<int:id>/", views.delete_group),
]