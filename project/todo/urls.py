from django.urls import re_path, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from rest_framework import permissions, routers
from rest_framework.routers import SimpleRouter
from todo import views


# Remove final trailing slash
class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()

router.register(r'^task', views.ReadViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^$', views.status),
    re_path(r'^ping', views.ping),
    re_path(r'^admin', admin.site.urls),
]

# Serve static
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, 
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, 
            {'document_root': settings.STATIC_ROOT}),
]
