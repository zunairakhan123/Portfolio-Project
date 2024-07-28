from django.urls import path
from .views import home, about,project,contact

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("project/",project,name="project"),
    path("contact/",contact, name="contact"),
]
