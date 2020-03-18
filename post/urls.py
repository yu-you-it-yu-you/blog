from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$', views.queryAll),
    url(r'^page/(\d+)$', views.queryAll),
    url(r'^post/(\d+)$', views.deteil),
    url(r'^category/(\d+)$',views.queryPostByCid),
    url(r'^archive/(\d+)/(\d+)$',views.queryPostByCreated),
]