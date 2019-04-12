from django.conf.urls import url
from system0 import views
urlpatterns=[
    url(r'^$',views.sysInfo),
]