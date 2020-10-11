from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'aluminum'
urlpatterns = [
    path('', 
        views.ExtruderListView.as_view(), 
        name='index'),
    path('<int:extruder_pk>/systems/', 
        views.ProductSystemListView.as_view(), 
        name='systems'),
    path('<int:extruder_pk>/<int:system_pk>/profiles/', 
        views.ProfileListView.as_view(), 
        name='profiles'),
    path('<int:extruder_pk>/<int:system_pk>/<int:pk>/detail/', 
        views.ProfileDetailView.as_view(), 
        name='detail'),
    path('create_extruder/', 
        views.CreateExtruderView.as_view(), 
        name='create_extruder'),
    path('<int:pk>/edit_extruder/', 
        views.EditExtruderView.as_view(), 
        name='edit_extruder'),
    path('<int:pk>/delete_extruder/', 
        views.DeleteExtruderView.as_view(), 
        name='delete_extruder'),
    path('<int:extruder_pk>/create_system/', 
        views.CreateProductSystemView.as_view(), 
        name='create_system'),
    path('<int:extruder_pk>/<int:pk>/edit_system/', 
        views.EditProductSystemView.as_view(), 
        name='edit_system'),
    path('<int:extruder_pk>/<int:pk>/delete_system/', 
        views.DeleteProductSystemView.as_view(), 
        name='delete_system'),
    path('<int:extruder_pk>/<int:system_pk>/create_profile/', 
        views.CreateProfileView.as_view(), 
        name='create_profile'),
    path('<int:extruder_pk>/<int:system_pk>/<int:pk>/edit_profile/', 
        views.EditProfileView.as_view(), 
        name='edit_profile'),
    path('<int:extruder_pk>/<int:system_pk>/<int:pk>/delete_profile/', 
        views.DeleteProfileView.as_view(), 
        name='delete_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
