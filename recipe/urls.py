from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("main/", views.main, name="main"),
    path("category_list/", views.category_list, name="category_list"),
]
