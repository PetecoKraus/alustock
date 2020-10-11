from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Extruder, ProductSystem, Profile
from .forms import ExtruderForm, ProductSystemForm, ProfileForm


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
        return ProductSystem.objects.filter(extruder__pk=self.kwargs['extruder_pk'])

    def get_context_data(self, **kwargs):
        context = super(ProductSystemListView, self).get_context_data(**kwargs)
        context['extruder_id'] = self.kwargs['extruder_pk']
        context['extruder_name'] = Extruder.objects.filter(id=self.kwargs['extruder_pk'])[0].extruder_name
        return context


class ProfileListView(generic.ListView):
    model = Profile
    template_name = 'aluminum/profiles.html'
    context_object_name = 'profiles_list'

    def get_queryset(self):
        return Profile.objects.filter(system__pk=self.kwargs['system_pk'])

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['system_id'] = self.kwargs['system_pk']
        context['system_name'] = ProductSystem.objects.filter(id=self.kwargs['system_pk'])[0].system_name
        context['extruder_id'] = self.kwargs['extruder_pk']
        return context


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'aluminum/detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['system_id'] = self.kwargs['system_pk']
        context['extruder_id'] = self.kwargs['extruder_pk']
        return context


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
        return reverse_lazy('aluminum:systems', kwargs={'extruder_pk': self.kwargs['pk']})


class DeleteExtruderView(generic.DeleteView):
    template_name = 'aluminum/delete_extruder.html'
    model = Extruder
    success_url = reverse_lazy('aluminum:index')
    context_object_name = 'extruder'


class CreateProductSystemView(generic.CreateView):
    template_name = 'aluminum/create_system.html'
    model = ProductSystem
    form_class = ProductSystemForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('aluminum:systems', kwargs={'extruder_pk': self.kwargs['extruder_pk']})


class EditProductSystemView(generic.UpdateView, SuccessMessageMixin):
    template_name = 'aluminum/edit_system.html'
    model = ProductSystem
    form_class = ProductSystemForm
    success_message = 'The system was successfully updated'
    context_object_name = 'system'

    def get_context_data(self, **kwargs):
        context = super(EditProductSystemView, self).get_context_data(**kwargs)
        context['system_id'] = self.kwargs['pk']
        context['extruder_id'] = self.kwargs['extruder_pk']
        return context

    def get_success_url(self):
        return reverse_lazy('aluminum:profiles', kwargs={'extruder_pk': self.kwargs['extruder_pk'],
                                                        'system_pk': self.kwargs['pk']})


class DeleteProductSystemView(generic.DeleteView):
    template_name = 'aluminum/delete_system.html'
    model = ProductSystem
    context_object_name = 'system'

    def get_context_data(self, **kwargs):
        context = super(DeleteProductSystemView, self).get_context_data(**kwargs)
        context['system_id'] = self.kwargs['pk']
        context['extruder_id'] = self.kwargs['extruder_pk']
        return context

    def get_success_url(self):
        return reverse_lazy('aluminum:systems', kwargs={'extruder_pk': self.kwargs['extruder_pk']})


class CreateProfileView(generic.CreateView):
    template_name = 'aluminum/create_profile.html'
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('aluminum:profiles', kwargs={'extruder_pk': self.kwargs['extruder_pk'],
                                                        'system_pk': self.kwargs['system_pk']})


class EditProfileView(generic.UpdateView, SuccessMessageMixin):
    template_name = 'aluminum/edit_profile.html'
    model = Profile
    form_class = ProfileForm
    success_message = 'The profile was successfully updated'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        context['profile_id'] = self.kwargs['pk']
        context['system_id'] = self.kwargs['system_pk']
        context['extruder_id'] = self.kwargs['extruder_pk']
        print(context)
        return context

    def get_success_url(self):
        return reverse_lazy('aluminum:detail', kwargs={'extruder_pk': self.kwargs['extruder_pk'],
                                                        'system_pk': self.kwargs['system_pk'],
                                                        'pk': self.kwargs['pk']})


class DeleteProfileView(generic.DeleteView):
    template_name = 'aluminum/delete_profile.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(DeleteProfileView, self).get_context_data(**kwargs)
        context['profile_id'] = self.kwargs['pk']
        context['system_id'] = self.kwargs['system_pk']
        context['extruder_id'] = self.kwargs['extruder_pk']
        return context

    def get_success_url(self):
        return reverse_lazy('aluminum:profiles', kwargs={'extruder_pk': self.kwargs['extruder_pk'],
                                                        'system_pk': self.kwargs['system_pk']})
