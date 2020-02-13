from django.conf.urls import url
from django.conf import settings
from mysite import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^post/$', views.PostCreate.as_view(), name='post_new'),
    url(r'^signup/$',views.registration, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^insta/$', views.SiteView.as_view(), name='insta'),
    url(r'^$', views.home_page, name='homePage'),
    url(r'^logout/$', auth_views.logout, {"next_page": '/'}, name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)