from django.conf.urls import url 
from . import views

app_name = 'acount_app'

urlpatterns = [
    url(r'^register/$', views.registration, name="register"),
    url(r'^user_login/$', views.user_login, name='user_login'),
    # url(r'^logout-then-login/$', django.contrib.auth.views.logout_then_login, name='logout_then_login'),
    url(r'^$', views.user_dashboard, name='dashboard'),
    url(r'^special/$', views.special_msg, name='special'),  
]
