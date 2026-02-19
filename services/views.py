from django.shortcuts import render, HttpResponse, redirect
from .models import services
from .forms import ServicesForm
# Create your views here.

def servicesList(request):
    all_services = services.objects.all()
    return render(request, 'services/servicesList.html',{"services":all_services})

def createServicesForm(request):
    print(request.method)
    if request.method == "POST":
        form = ServicesForm(request.POST)
        form.save() #it same as create
        return HttpResponse("SERVICES CREATED....")
    else:
        #form object create --> html
        form = ServicesForm()   #form object  
        return render(request, "services/createServicesForm.html", {"form":form})
    
def deleteServices(request,id):
    print("id from url = ",id)
    services.objects.filter(id=id).delete()
    return redirect("servicesList") #url --> name -->    

def updateServices(request,id):
    #database existing user... id -->
    update_services = services.objects.get(id=id) #select * from employee where id = 1
    
    if request.method == "POST":
        form = ServicesForm(request.POST,instance=update_services)
        form.save()
        return redirect("servicesList")
    else:
        form = ServicesForm(instance=update_services)    
        return render(request,"services/updateServices.html",{"form":form})