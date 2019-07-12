from django.contrib import admin
from django.conf.urls import url

import hello.views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^hello/', hello.views.hello),
]
