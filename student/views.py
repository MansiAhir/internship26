from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request,"studentHome.html")

def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student)

def studentMarks(request):
    student1 = {"name":"Rajvi","marks":87}
    return render(request,"student/studentMarks.html",student1)

def studentAttendance(request):
    student2 = {"name":"Tanya","attendance":75}
    return render(request,"student/studentAttendance.html",student2)

def studentFees(request):
    student3 = {"name":"john","fees":45000}
    return render(request,"student/studentFees.html",student3)