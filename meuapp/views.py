from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def segundo(request):
    return render(request, "segundo_site.html")


