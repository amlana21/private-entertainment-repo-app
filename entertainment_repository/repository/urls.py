from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("indexpage/", views.homepage, name="homepage"),
    path("searchitems/", views.searchitems, name="searchitems"),
    path("additems/", views.additems, name="additems"),
    path("logout_view/", views.logout_view, name="logout_view")
    
]