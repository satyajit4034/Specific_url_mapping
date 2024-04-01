from django.shortcuts import render

# Create your views here.
def microsoft(request):
    return render(request,'microsoft.html')
def apple(request):
    return render(request,'apple.html')