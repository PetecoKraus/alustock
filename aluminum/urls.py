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
    path('create_extruder/', views.CreateExtruderView.as_view(), name='create_extruder'),
    path('<int:pk>/edit_extruder/', views.EditExtruderView.as_view(), name='edit_extruder'),
    path('<int:pk>/delete_extruder/', views.DeleteExtruderView.as_view(), name='delete_extruder'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
