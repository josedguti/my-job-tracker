from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import List


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)
    else:
        lists = None
    return render(request, 'index.html', {
        'lists': lists
    })
    
 
def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        # sign up the user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # give the user a fresh form to fill out
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form })


class CreateList(CreateView, LoginRequiredMixin):
    model = List
    fields = ['companyname', 'date']
    success_url = '/'  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  

class UpdateList(UpdateView, LoginRequiredMixin):
    model = List
    fields = ('companyname', 'date', 'contacted', 'interviewed')
    success_url = '/'

class DeleteList(DeleteView, LoginRequiredMixin):
    model = List
    success_url = '/'