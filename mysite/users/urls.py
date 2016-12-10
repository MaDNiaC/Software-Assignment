from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import signup	

urlpatterns = [
    url(r'^register/$', signup),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/users/login'}, name='logout'),
    url(r'', include("django.contrib.auth.urls"))


]

