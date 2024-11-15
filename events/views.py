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

    def form_valid(self, form):
        form.instance.group_id = self.request.GET.get('group') 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('group_detail', kwargs={'group_id': self.object.group.id})


# Create your views here.
