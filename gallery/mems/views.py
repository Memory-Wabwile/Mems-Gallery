from django.shortcuts import render
from django.http  import HttpResponse



# Create your views here.
def welcome(request):
    '''
    the view function
    '''
    return HttpResponse('Welcome to Mems gallery')

def mems_home(request):
    '''
    finction to display images on the home page
    '''

    return render(request, 'index.html', {'location':location, 'category': category,'pictures':pictures})
                                         
                                          