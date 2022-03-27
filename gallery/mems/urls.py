from django.urls import path , re_path
from . import views

#urlpatterns for a list of urls in our app
urlpatterns=[
    # path('',views.welcome,name = 'welcome'),
    path('' , views.mems_home, name = 'memsHome'),
    path('searched/',views.search_results,name='search_results'),
    re_path(r'^images/(\d+)',views.image,name ='image')
    
]