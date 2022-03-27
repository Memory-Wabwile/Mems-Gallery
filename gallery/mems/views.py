from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image




# Create your views here.
def welcome(request):
    '''
    the view function
    '''
    return HttpResponse('Welcome to Mems gallery')

def mems_home(request):
    '''
    function to display images on the home page
    '''
    
    return render(request, 'index.html')
    
                                         
                                          