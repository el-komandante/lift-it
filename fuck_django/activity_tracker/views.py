from django.shortcuts import render
from . import views
from django.conf.urls import url

def index(request):
    return render(request, 'activity_tracker/index.html')

# urlpatterns = patterns('',
#     url(r^'login/$', 'django.contrib.auth.views.login'),
#     url(r^'logout/$', 'django.contrib.auth.views.logout'),
# )
