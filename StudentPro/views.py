from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #sid = request.GET["id"]
   # student = Student.objects.get(1)
   # print(student)
   # context = {
    #    'student': student
    #}      , context
    return render(request,'studentHome.html')
def attend(request):
    return render(request,'studentAttend.html')