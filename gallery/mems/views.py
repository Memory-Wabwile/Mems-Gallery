from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image
from django.core.exceptions import ObjectDoesNotExist




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
    image = Image.highlights()
    message = "There's nothing to show"
    return render(request, 'index.html' , {"image" : image , "message":message})
    
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
                                         
def image(request, id):
    try:
        image = Image.objects.get(pk = id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'image.html', {"image": image})
                                          