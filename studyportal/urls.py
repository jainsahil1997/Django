"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
app_name= 'studyportal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<department_id>[0-9]+)/$',views.subject, name='subject'),
    url(r'^(?P<department_id>[0-9]+)/(?P<subject_code>[\w\-]+)/$',views.material, name='material'),
    url(r'material/add/$',views.MaterialCreate.as_view(),name='material-add'),
    url(r'^accounts/',include('registration.backends.hmac.urls')),
    url(r'^material/add/$', views.model_form_upload, name='create_material'),


]
