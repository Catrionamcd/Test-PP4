from . import views
from django.urls import path

urlpatterns = [
    path('', views.ChannelList.as_view(), name='home'),
]
