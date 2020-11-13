from django.conf.urls import url 
from videos import views 
 
urlpatterns = [ 
    url(r'^api/history$', views.history_list),
    url(r'^api/history/(?P<pk>[0-9]+)$', views.history_detail),
    url(r'^api/bookmark$', views.bookmark_list),
    url(r'^api/bookmark/(?P<pk>[0-9]+)$', views.bookmark_detail),
    url(r'^api/totalbookmark$', views.bookmark_total),
]