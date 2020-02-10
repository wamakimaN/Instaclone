from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home_page, name='homePage'),
    url(r'^insta/$', views.SiteView.as_view(), name='insta'),
] 