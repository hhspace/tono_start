from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]