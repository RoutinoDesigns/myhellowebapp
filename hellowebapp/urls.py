
from django.conf.urls import url
from django.contrib import admin

from collection import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='home',
    ),
    url(r'^admin/', admin.site.urls),
]