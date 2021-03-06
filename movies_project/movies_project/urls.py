"""movies_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movies.views import MoviesView, MovieView, PeopleView, PersonView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', MoviesView.as_view()),
    url(r'^movie/(?P<id>\d+)/$', MovieView.as_view()),
    url(r'^people/$', PeopleView.as_view()),
    url(r'^person/(?P<id>\d+)/$', PersonView.as_view()),
]
