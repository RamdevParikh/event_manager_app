from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/detail.html', {'event': event})

def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})

def update(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/update.html', {'form': form})

def delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('index')
    return render(request, 'events/delete.html', {'event': event})
