from django import forms
from .models import Employee, Course, Event, Book

#employee form
#modelForm -->it will create form using model fileds

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book     
        fields = '__all__'   