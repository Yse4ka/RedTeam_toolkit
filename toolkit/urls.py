from django.urls import path
from . import views
from .scripts import *

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fullscan/', views.fullscan, name='fullscan'),
    path('livehost/', views.livehost, name='livehost'),
    path('dirscan/', views.dirscan, name='dirscan'),
    path('cvedes/', views.cvedes, name='cvedes'),
    path('linux/', views.linux, name='linux'),
    path('windows/', views.windows, name='windows'),
    path('sshbruteforce/', views.sshbruteforce, name='sshbruteforce'),
    path('windows/nightmare/', views.nightmare, name='nightmare'),
    path('windows/rdpbruteforce/', views.rdpbruteforce, name='rdpbruteforce'),
    path('download/', views.download_file, name='download_file'),
    path('stream/', views.stream, name='stream'),
    #<str:filepath>/
]
