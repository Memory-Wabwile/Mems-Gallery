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
    
    return render(request, 'index.html' , {"image" : image })
    
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_location(request):

    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        search_location = Image.filter_by_location(location)
        message = f"{location}"

        return render(request, 'location.html',{"message":message,"search_location": search_location})

    else:
        message = "You haven't searched for any location"
        return render(request, 'location.html',{"message":message})

# def search_location(request,location):
#     images = Image.filter_by_location(location)
#     return render(request, 'location.html', {'locations': images}) 

def image(request, id):
    try:
        image = Image.objects.get(pk = id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'image.html', {"image": image})
                                          