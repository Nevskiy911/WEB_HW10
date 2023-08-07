from django.urls import path

from . import views


app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:text>", views.main, name="root_paginate"),
]
