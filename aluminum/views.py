from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Extruder, ProductSystem, Profile
from .forms import ExtruderForm


class ExtruderListView(generic.ListView):
    template_name = 'aluminum/index.html'
    context_object_name = 'extruders_list'

    def get_queryset(self):
        return Extruder.objects.order_by('extruder_name')[:20]


class ProductSystemListView(generic.ListView):
    model = ProductSystem
    template_name = 'aluminum/systems.html'
    context_object_name = 'systems_list'

    def get_queryset(self):
        return ProductSystem.objects.filter(extruder__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProductSystemListView, self).get_context_data(**kwargs)
        context['extruder_id'] = self.kwargs['pk']
        context['extruder_name'] = Extruder.objects.filter(id=self.kwargs['pk'])[0].extruder_name
        print(context)
        return context


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


class CreateExtruderView(generic.CreateView):
    template_name = 'aluminum/create_extruder.html'
    success_url = reverse_lazy('aluminum:index')
    model = Extruder
    form_class = ExtruderForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditExtruderView(generic.UpdateView, SuccessMessageMixin):
    template_name = 'aluminum/edit_extruder.html'
    model = Extruder
    form_class = ExtruderForm
    success_message = 'The extruder was successfully updated'
    context_object_name = 'extruder'

    def get_success_url(self):
          extruder_id = self.kwargs['pk']
          return reverse_lazy('aluminum:systems', kwargs={'pk': extruder_id})


class DeleteExtruderView(generic.DeleteView):
    template_name = 'aluminum/delete_extruder.html'
    model = Extruder
    success_url = reverse_lazy('aluminum:index')
    context_object_name = 'extruder'