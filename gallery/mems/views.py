from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    '''
    the view function
    '''
    return HttpResponse('Welcome to Mems gallery')