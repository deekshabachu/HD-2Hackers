from django.shortcuts import render



from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h1>Smart Chemical & Equipment Inventory System</h1>"
        "<p>Backend is working. UI phase started.</p>"
    )

