from django.shortcuts import render
from .models import Technology

# Create your views here.
def home(request):
    return render(request, 'home.html')

def technologies(request):
    if request.method == 'GET':
        technologies = Technology.objects.all()
        return render(request, 'technologies.html', {'technologies': technologies})
    elif request.method == 'POST':
        request_data = request.POST
        technology_name = request_data.get('technology_name')
        technology_description = request_data.get('technology_description')
        Technology.objects.create(name=technology_name, description=technology_description)
        return render(request, 'technologies.html', {'technologies': Technology.objects.all()})
    else:
        return render(request, 'technologies.html', {'technologies': Technology.objects.all()})
    