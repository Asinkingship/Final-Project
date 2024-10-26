from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Event
from .forms import EventCreateForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class EventListView(ListView):
    template_name = 'events/list.html'
    model = Event

class EventDetailView(DetailView):
    template_name = 'events/details.html'
    model = Event

class CreateEventView(CreateView):
    template_name = 'events/create_event.html'
    form_class = EventCreateForm

    def get_success_url(self):
        return reverse('events_list')

# Create your views here.
