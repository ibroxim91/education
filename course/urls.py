from django.urls import path
from .views import all_courses


urlpatterns = [
    path('', all_courses ),

]  