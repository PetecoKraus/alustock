from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'aluminum'
urlpatterns = [
    path('', views.ExtruderListView.as_view(), name='index'),
    path('<int:pk>/systems/', views.ProductSystemListView.as_view(), name='systems'),
    path('<int:pk>/profiles/', views.ProfileListView.as_view(), name='profiles'),
    path('<int:pk>/detail/', views.ProfileDetailView.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
