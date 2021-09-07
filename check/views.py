from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def Verif(request):
    return render(request,'check/ajouter.html')