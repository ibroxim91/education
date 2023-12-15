from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from course.models import Course , Category , Gallery

# Create your views here.

def home(request):
    course_all = Course.objects.all()
    category_all = Category.objects.all()
    photos = Gallery.objects.all() 
    context = {"courses": course_all , "category_all":category_all ,"photos_all":photos}
    return render(request, "index.html", context)


def category_courses(request, id):
    c = Category.objects.get(id=id) #get_object_or_404( Category , id=id) 
    courses = Course.objects.filter(category=c)
    category_all = Category.objects.all()
    
    context = {"courses": courses,  "category_all":category_all }
    return render(request, "category.html", context)


