from django.contrib import admin
from .models import Course, Category, CourseVideos

# Register your models here.


class CourseVideosAdmin(admin.TabularInline):
    model = CourseVideos


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category","price")
    list_editable = ("price",)
    list_display_links = ("title",)
    search_fields = ("title","price")
    list_filter = ("category","price")
    inlines = [CourseVideosAdmin]


admin.site.site_header = "Kurslar"