from django.shortcuts import render
from . import helpers
# Create your views here.
def home(request):
    if request.method == 'POST':
        technologies = request.POST['technology']
        prompt = request.POST['idea']
        response = helpers.get_response(prompt, technologies)
        return render(request, 'home.html', {'response': response})
    return render(request, 'home.html')