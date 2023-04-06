from django.shortcuts import HttpResponseRedirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accountapp.models import HelloWWorld

# Create your views here.

def hello_world(request):
    
    if request.method == "POST":
        temp=request.POST.get('hello_world_input')
        new_hello_world = HelloWWorld()
        new_hello_world.text=temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        

