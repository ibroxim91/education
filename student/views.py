from django.shortcuts import render,get_object_or_404, redirect

from django.http import HttpResponseRedirect
from django.urls import reverse


from course.models import Course , Category , Gallery

from django.contrib.auth.views import LoginView


# Create your views here.

def home(request):
    print()
    print( request.user)
    print()
    # if  request.user.is_authenticated:
    #     return HttpResponseRedirect( reverse("student:login") )

    
    course_all = Course.objects.all()
    category_all = Category.objects.all()
    photos = Gallery.objects.all() 
    context = {"courses": course_all , "category_all":category_all ,"photos_all":photos}
    # return HttpResponseRedirect("https://uzum.uz")


    return render(request, "index.html", context)


def category_courses(request, id):
    c = Category.objects.get(id=id) #get_object_or_404( Category , id=id) 
    courses = Course.objects.filter(category=c)
    category_all = Category.objects.all()
    
    context = {"courses": courses,  "category_all":category_all }
    return render(request, "category.html", context)



class  MyLoginView(LoginView):
    pass
    # redirect_authenticated_user = "/"
    # template_name = "auth/login.html"
