from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'serv/about.html')

def contact(request):
    return render(request,'serv/contact.html')