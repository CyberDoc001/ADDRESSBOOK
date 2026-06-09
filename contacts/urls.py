from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/new/', views.contact_create, name='contact_create'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('contact/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/new/', views.group_create, name='group_create'),
    path('groups/<int:pk>/edit/', views.group_edit, name='group_edit'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),
]
