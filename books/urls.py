from django.conf.urls import url
from .views import search_form, search

urlpatterns = [
    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
]
