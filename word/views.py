from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Daily_words
from django.contrib.auth.forms import UserCreationForm
from  django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
class HomePage(ListView):
    model=Daily_words
    context_object_name='word'
    template_name='Home.html'
    id=True
class WordPage(DetailView):
    model=Daily_words
    context_object_name='word'
    template_name='word.html'

class AddWord(CreateView):
    model=Daily_words
    context_object_name='word'
    template_name='new_word.html'
    fields='__all__'

class UpdateWord(UpdateView):
    model=Daily_words
    context_object_name='word'
    template_name='editword.html'
    fields=['Word','Meaning']
class DeleteWord(DeleteView):
    model=Daily_words
    context_object_name='word'
    template_name='delete.html'
    success_url=reverse_lazy('HOME')

class SignUp(CreateView):
     form_class=UserCreationForm
     template_name='signup.html'
     success_url=reverse_lazy('login')
