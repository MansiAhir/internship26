from django.contrib import admin
from .models import Employee, Course, Event, Book
# Register your models here.

admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Book)