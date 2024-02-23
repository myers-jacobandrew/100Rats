"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from a_posts.views import *

urlpatterns = [
    #path('page-name', html_page_name, name='page-name')
    #path('',name=''),
    path('admin/', admin.site.urls),
    path('', home_view),
    path('monster/create/', create_monster_view, name='create-monster'),
    path('view/monsters/', view_all_monsters, name='view-all-monsters'),
    path('monster/create/manual-input-form/', manual_input_form_view, name='manual-input-form'),
    path('monster/create/automatic-input-form/', automatic_input_form_view, name='automatic-input-form'),
    path('monster/create/manual-data-entered/', manual_data_entered_view, name='manual-data-entered'),
    path('monster/create/automatic-data-entered/', automatic_data_entered_view, name='automatic-data-entered'),
]
