from django.shortcuts import render

# Create your views here.
def students1(request):
    return render(request,'SecondApp/students.html')
def students2(request):
    return render(request,'SecondApp/students2.html')

