from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # View all events
    path('event/<int:id>/', views.detail, name='detail'),  # View event details
    path('create/', views.create, name='create'),  # Create an event
    path('update/<int:id>/', views.update, name='update'),  # Update an event
    path('delete/<int:id>/', views.delete, name='delete'),  # Delete an event
]
