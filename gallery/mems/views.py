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
    
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
                                         
                                          