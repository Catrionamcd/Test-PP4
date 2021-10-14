from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views import generic
from .models import Channel


# class HomeView(TemplateView):
#     template_name = 'base.html'


class ChannelList(generic.ListView):
    model = Channel
    queryset = Channel.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
