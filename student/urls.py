from django.urls import path 
from .views import home, category_courses,MyLoginView,register_view ,TestView



app_name = "student"

urlpatterns = [
   
    path('', home ),
    path('category/<int:id>', category_courses ,name="category_detail" ),
    path('kirish', MyLoginView.as_view()  , name="login" ),
    path('register', register_view  , name="register" ),
    path('test',  TestView.as_view() , name="test" ),
]