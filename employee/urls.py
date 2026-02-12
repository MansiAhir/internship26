from . import views
from django.urls import path

urlpatterns = [
    path('employeeList/', views.employeeList,name="employeeList"),
    path('employeeFilter/', views.employeeFilter),
    path('createemployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
    path('createCourse/',views.createCourse),
    path('createEvent/',views.createEvent),    
    path('createBook/',views.createBook),
    path('deleteEmployee/<int:id>',views.deleteEmployee,name="deleteEmployee"),
    path('filterEmployee/',views.filterEmployee,name="filterEmployee"),
   path('sortEmployees/<int:id>', views.sortEmployees, name='sortEmployees'),


]