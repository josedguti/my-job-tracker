from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import List


# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'lists': List.objects.all()
    })
    
 
def about(request):
    return render(request, 'about.html')


class CreateList(CreateView):
    model = List
    fields = ['companyname', 'date']
    success_url = '/'    