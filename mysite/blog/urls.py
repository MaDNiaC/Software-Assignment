from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', show_entries),
    url(r'^(?P<todo_id>[0-9]+)', get_entry),
    url(r'^all/$', show_all_entries),
    url(r'^all/user/(?P<userId>[0-9]+)$', show_all_entries_from_user),
]
