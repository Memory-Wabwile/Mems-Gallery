from django.urls import path
from . import views

#urlpatterns for a list of urls in our app
urlpatterns=[
    path('',views.welcome,name = 'welcome'),
]