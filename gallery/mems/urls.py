from django.conf import settings
from django.urls import path , re_path
from . import views
from django.conf.urls.static import static

#urlpatterns for a list of urls in our app
urlpatterns=[
    # path('',views.welcome,name = 'welcome'),
    path('' , views.mems_home, name = 'memsHome'),
    path('searched/',views.search_results,name='search_results'),
    re_path(r'^images/(\d+)',views.image,name ='image')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)