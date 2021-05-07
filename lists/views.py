from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class UpdateList(UpdateView):
    model = List
    fields = ('companyname', 'date', 'contacted', 'interviewed')
    success_url = '/'

class DeleteList(DeleteView):
    model = List
    success_url = '/'