from django.db import models
from django.contrib.auth.models import User
import datetime

free = datetime.timedelta(days=5)
# Create your models here.

# ORM  Object Relation Mapping

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                 related_name="student" , null=True)
    status = models.BooleanField(verbose_name="Statusi", default=False)
    phone = models.CharField(max_length=15 , blank=True)
    brith_date = models.DateField(blank=True)
    adress = models.CharField(max_length=255)

    #  phone = models.TextField( blank=True)
    # models.EmailField(unique=True, max_length=55)
    # models.IntegerField(default=0)
    # models.SmallIntegerField(default=0)
    # models.BigIntegerField(default=0)
    # models.PositiveIntegerField()
    # models.SlugField(unique=True, max_length=55)
    # models.TimeField()
    # models.DateField()
    # models.DateTimeField(auto_now_add=True)
    # models.DecimalField(max_digits=5, decimal_places=3)
    # models.DurationField("days = 1")


    # models.ForeignKey(Category , on_delete=models.SET_NULL, )
    # models.ManyToManyField(Category , on_delete=models.SET_NULL, )
    # models.ImageField(upload_to="/images")
    # models.FileField(upload_to="/file")








