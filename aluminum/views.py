from django.http import HttpResponse
from django.views import generic

from .models import Profile

class IndexView(generic.ListView):
    template_name = 'aluminum/index.html'
    context_object_name = 'profiles_list'
    def get_queryset(self):
        return Profile.objects.order_by('-profile_code')[:20]