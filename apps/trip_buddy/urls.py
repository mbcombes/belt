from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),                # /
    url(r'^create$', views.create),         # /create
    url(r'^login$', views.login),           # /login
    url(r'^dashboard$', views.dashboard),   # /dashboard
    url(r'^destroy$', views.destroy),       # /destroy
    url(r'^trips/new$', views.newtrip),     # /trips/new
    url(r'^trips/(?P<id>\d+)/destroy$', views.destroy_trip),    # /trips/<id>/destroy
    url(r'^trips/(?P<id>\d+)/edit$', views.edit_trip),          # /trips/<id>/edit
    url(r'^trips/update', views.update_trip),                   # /trips/update
    url(r'^trips/(?P<id>\d+)$', views.view),                    # /trips/<id>
    url(r'^trips/create$', views.create_trip),                  # /trips/create
    url(r'^trips/(?P<id>\d+)/join$', views.join),               # /trips/<id>/edit
    url(r'^trips/(?P<id>\d+)/cancel$', views.cancel), 

]
