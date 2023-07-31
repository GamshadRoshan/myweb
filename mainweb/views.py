from django.shortcuts import render

# Create your views here.
def webhome(request):
    return render(request, 'mainweb/mainweb.html')