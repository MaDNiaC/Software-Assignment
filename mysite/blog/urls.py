from django.conf.urls import url

from .views import show_entries, get_entry

urlpatterns = [
    url(r'^$', show_entries),
    url(r'^(?P<todo_id>[0-9]+)', get_entry)
]
