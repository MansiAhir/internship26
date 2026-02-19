from django.urls import path
from . import views

urlpatterns = [
       path('servicesList/', views.servicesList,name="servicesList"),
       path('createServicesForm/', views.createServicesForm,name="createServicesForm"),
       path('deleteServices/<int:id>', views.deleteServices,name="deleteServices"),
       path('updateServices/<int:id>', views.updateServices,name="updateServices"),
]
