from django.shortcuts import render
from .models import Twice #이거꼭해줘야함

# Create your views here.

def twice(request):
    members = Twice.objects.filter(nationality='JP')
    return render(request, 'home.html', {'japanese' : members} )