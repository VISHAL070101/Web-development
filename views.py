from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request,"trav/front.html")


def agentlog(request):
    return render(request,"trav/agentlogin.html")


def agentreg(request):
    return render(request,"trav/agentreg.html")


def passlog(request):
    return render(request,"trav/passengerlogin.html")


def passreg(request):
    return render(request,"trav/passengerreg.html")