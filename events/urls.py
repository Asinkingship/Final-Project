from django.urls import path
import events.views as view
from .views import EventCreateForm, CreateEventView


urlpatterns = [
    path('', view.HomePageView.as_view(), name='home'),
    path('about/', view.AboutPageView.as_view(), name='about'),
    path('list/', view.EventListView.as_view(), name='events_list'),
    path('details/<int:pk>/', view.EventDetailView.as_view(), name='event_detail'), 
    path('create/', CreateEventView.as_view(), name='create_event'),  
]