from django.conf.urls import url
from .views import index
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', index, name='index')

]