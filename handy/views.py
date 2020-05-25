from django.http import HttpResponse
from django.shortcuts import render
from handy.models import Contractor


def index(request):
    
    data = Contractor.objects.all()
    print(data[1].name)
    print(data[2].name)

    context={
      'data': data
    }

    return render(request, 'index.html', context)