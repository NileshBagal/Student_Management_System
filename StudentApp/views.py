from django.shortcuts import render
from django.http import HttpResponse
def login(request):
    #sid = request.GET["id"]
   # student = Student.objects.get(1)
   # print(student)
   # context = {
    #    'student': student
    #}      , context
    return render(request,'login.html')
def attend(request):
    return render(request,'studentAttend.html')
def viewnotice(request):
    return render(request,'studentNotice.html')
def parent(request):
    return render(request,'studentParent.html')
def dashboard(request):
    return render(request,'dashboard.html')
def profile(request):
    return render(request,'studentHome.html')
def index(request):
    if request.method == ["POST"]:
        a = request.GET['usertype']
        print(a)
        print(request.GET['name'])