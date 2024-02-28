from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, template_name="home.html")


def add(request):
    x = request.GET["t1"]
    y = request.GET["t2"]
    i = int(x)
    j = int(y)
    k = i + j
    return HttpResponse("<html><h2>The sum is:</h2></html>"+ str(k))
