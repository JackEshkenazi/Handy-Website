from django.http import HttpResponse
from django.shortcuts import render
from handy.models import Contractor


def index(request):
    
  dataContractors = Contractor.objects.all()

  dataCities = Contractor.city.through.objects.all()

  #print(data[2])

  context={
    "data": dataContractors,
    "cities": dataCities
  }

  return render(request, 'index.html', context)

def contact(request):

  return render(request, 'contact.html')