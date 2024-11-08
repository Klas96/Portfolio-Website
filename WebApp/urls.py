"""
URL configuration for PersonalWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from PersonalWebsite.views import index, code_page, art_page, timeline

print("Loading URLs...")  # Debugging statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Home page
    path('code/', code_page, name='code_page'),  # Code portfolio page
    path('art/', art_page, name='art_page'),  # Art portfolio page
    path('timeline/', timeline, name='timeline'),  # Timeline page
]

print("URLs loaded.")  # Debugging statement