from appTwo import views
from django.conf.urls import url


urlpatterns = [
    url('', views.user, name = 'user'),
    
]
