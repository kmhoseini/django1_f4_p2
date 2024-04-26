from django.contrib import admin
from django.urls import path
from resumeapp.views import  *
app_name="myresume"
urlpatterns = [ path('',home_view,name='index'),
                path('skill',skill_view,name='skill'),
                path('language',lang_view,name='lang'),
                path('bio',bio_view,name='bio'),
                path('study',study_view,name='study')]
