from django.urls import path 
from .views import home, category_courses

urlpatterns = [
   
    path('', home ),
    path('category/<int:id>', category_courses ),
]