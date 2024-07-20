from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'varVal':"this is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicespage")

def contact(request):
    return HttpResponse("this is contactpage")