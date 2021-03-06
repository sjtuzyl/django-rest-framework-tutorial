from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # url(r'^snippets/$',views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail)
    url(r'^/$', views.api_root),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)