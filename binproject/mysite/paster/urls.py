from django.urls import path, re_path

from . import views

app_name='paster'
urlpatterns = [
    path('', views.root, name='root'),
    path('paste/', views.paste, name='paste'),
  	re_path(r'^(?P<rand_string>\S{10})/$', views.show, name='show'),
  	re_path(r'^(?P<rand_string>\S{10})/delete$', views.delete, name='delete'),
  	path('search/', views.search, name='search')
]