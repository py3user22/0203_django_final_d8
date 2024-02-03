from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '0203_django_notes2.html', {})

