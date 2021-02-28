from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Event
# Create your views here.

def index(request):
    events = Event.objects.all()
    param = {'events':events}
    return render(request, 'index.html', param) 

def addEvent(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            date = request.POST['date']
            time = request.POST['time']
            location = request.POST['location']
            image = request.FILES['image']

            newEvent = Event(name=name, date=date, time=time, location=location, img=image)
            newEvent.save()

            messages.info(request, 'Your event is registered successfully....')
            return redirect('/')

        except:
            messages.error(request, 'Something wend wrong')
            return redirect('/')    

    else:    
        return render(request, 'add.html')    

def like(request, id):
    eventTarget = Event.objects.filter(event_id=id)
    eventTarget.update(is_liked=True)
    return redirect('/')        

def dislike(request, id):
    eventTarget = Event.objects.filter(event_id=id)
    eventTarget.update(is_liked=False)
    return redirect('/')       