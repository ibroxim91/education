from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="courses")  
    title = models.CharField("Title", max_length=55) # Descriptor ORM
    image = models.ImageField(upload_to="Courses")
    duration = models.IntegerField("Months")
    author = models.ForeignKey("auth.User" , on_delete=models.CASCADE)
    price = models.PositiveIntegerField("Price") # Quantity

    def __str__(self):
        return self.title

class CourseVideos(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE)  
    name = models.CharField(max_length=20)
    video_file = models.FileField(upload_to="videos")
    
    def __str__(self):
        return f"{self.name} -> {self.course.title}"



class Gallery(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images")

    