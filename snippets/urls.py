from django.conf.urls import url
from snippets import views1

urlpatterns = [
    url(r'^snippets/$', views1.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views1.snippet_detail),
]