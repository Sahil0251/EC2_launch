from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'tittle':"Homepage | Sahil World",
        'bdata' : "About us",
        'clist':['PHP',"Jawa",'Django'],
        'student_details':[
            {'name':'pardeep','phone':9728000251},
            {'name':'Sahil', 'phone':9053113355}
        ]
    }
    return render(request, "index.html",data)

def aboutus(request):
    return HttpResponse("About us for sahil")

def course(request):
    return HttpResponse("Course available")

def coursedetail(request, courseid):
    return HttpResponse(courseid)
def coursedetails(request, courseid):
    return HttpResponse(courseid)