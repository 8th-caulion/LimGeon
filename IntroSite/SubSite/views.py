from django.shortcuts import render

def hobby(request):
    return render(request, 'hobby.html')

def personality(request):
    return render(request, 'personality.html')

def service(request):
    return render(request, 'service.html')
