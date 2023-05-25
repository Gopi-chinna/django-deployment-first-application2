from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
import datetime
import time
def wishes(request):
    return render(request,'FirstApp1/wishes1.html');
def hello(request):
    return render(request,'FirstApp1/hello.html');
def datetimefunction(request):
    date1=datetime.datetime.now()
    print(date1)
    date2=time.ctime()
    print(date2)
    rollno=1001;
    sname='Gopi';
    marks=99;
    dict1={"Gopi":date1,"Vedan":date2,'rollno':rollno,'sname':sname,'marks':marks}
    return render(request,'FirstApp1/datetime.html',dict1);
def wishes2(request):
    date1=datetime.datetime.now()
    msg1='Hello user/client....GOOD'
    hr=int(date1.strftime('%H'))
    if hr<12:
        msg1+='MORNING !!'
    elif hr<16:
        msg1+='AFTERNOON !!'
    elif hr<20:
        msg1+='EVENING !!'
    else:
        msg1+='Hello user/client....GOOD NIGHT !!'
    dict1={'date1':date1,'msg':msg1}
    return render(request,'FirstApp1/wishes2.html',context=dict1)
