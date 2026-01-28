from django.http import HttpResponse
from django.shortcuts import render

#specific url
def test(request):
    return HttpResponse("Hello")

# def Aboutus(request):
#     return HttpResponse("About")

def Aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def movies(request):
    return render(request,"movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")

def home(request):
    return render(request,"home.html")

def recap(request):
    return render(request,"recap.html")

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient}
    return render(request,"recipe.html",data)

def teams(request):
    playerlist = ["virat","Rohit","Shreyas","Dhoni","Abhishek"]
    trophy = ["t20","IPL","ODI"]
    data = {"teamname":"t20","capname":"Shubhman","playerlist":playerlist, "trophy":trophy}
    return render(request,"team.html",data)
