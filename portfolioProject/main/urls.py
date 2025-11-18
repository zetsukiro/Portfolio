from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('contact/', views.contact, name='contact'),

    # Add routes
    path('add-skill/', views.add_skill, name='add_skill'),
    path('add-tool/', views.add_tool, name='add_tool'),
    path('add-interest/', views.add_interest, name='add_interest'),
    path('add-experience/', views.add_experience, name='add_experience'),

    # Delete routes
    path('delete-skill/<int:id>/', views.delete_skill, name='delete_skill'),
    path('delete-tool/<int:id>/', views.delete_tool, name='delete_tool'),
    path('delete-interest/<int:id>/', views.delete_interest, name='delete_interest'),
    path('delete-experience/<int:id>/', views.delete_experience, name='delete_experience'),
]
