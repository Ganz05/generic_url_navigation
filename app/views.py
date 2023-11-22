from django.shortcuts import render

# Create your views here.
def Mom(request):
    return render(request,'Mom.html')

def Son(request):
    return render(request,'Son.html')
