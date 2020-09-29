from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Extruder, ProductSystem, Profile

class ExtruderListView(generic.ListView):
    template_name = 'aluminum/index.html'
    context_object_name = 'extruders_list'

    def get_queryset(self):
        return Extruder.objects.order_by('-extruder_name')[:20]


class ProductSystemListView(generic.ListView):
    model = ProductSystem
    template_name = 'aluminum/systems.html'
    context_object_name = 'systems_list'

    def get_queryset(self):
        return ProductSystem.objects.filter(extruder__pk=self.kwargs['pk'])


class ProfileListView(generic.ListView):
    model = Profile
    template_name = 'aluminum/profiles.html'
    context_object_name = 'profiles_list'

    def get_queryset(self):
        return Profile.objects.filter(system__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['system_id'] = self.kwargs['pk']
        return context


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'aluminum/detail.html'
    context_object_name = 'profile'
