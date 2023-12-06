from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Course(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)  
    title = models.CharField("Title", max_length=55) # Descriptor ORM
    image = models.ImageField(upload_to="Courses")
    duration = models.IntegerField("Months")
    author = models.ForeignKey("auth.User" , on_delete=models.CASCADE)
    price = models.PositiveIntegerField("Price") # Quantity

class CourseVideos(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE)  
    name = models.CharField(max_length=20)
    video_file = models.FileField(upload_to="videos")
