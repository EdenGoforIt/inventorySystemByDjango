from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    url(r'^$', index, name='index'),
    url(r'^display_product$', display_product, name='display_product'),
    url(r'^display_purchase$', display_purchase, name='display_purchase'),
    url(r'^display_order$', display_order, name='display_order'),
    url(r'^display_report$', display_report, name='display_report'), 

]
