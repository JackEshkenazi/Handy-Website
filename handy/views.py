from django.db.models.sql.datastructures import Join
from django.http import HttpResponse
from django.shortcuts import render
from handy.models import Contractor, City
from django.db.models.functions import Concat
from django.db.models import Aggregate, CharField, Value

class Card:
  name: str
  phone: str
  email: str
  cities = []



class GroupConcat(Aggregate):
    # supports COUNT(distinct field)
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(expression)s, "%(separator)s")'


    def __init__(self, expression, separator=',', **extra):
        super(GroupConcat, self).__init__(
            expression,
            separator=separator,
            output_field=CharField(),
            **extra
        )


def index(request):

  
  contractor_ids = Contractor.objects.only("contractor_id")

  cards = dict()
  query_result = Contractor.objects.annotate(cities=GroupConcat('city',separator=','))
  for row in query_result:
    print(row)
  
    
  # contractors = Contractor.objects.all()
  # cities = Cities.objects.all()
  # for contractor in contractors:
  #   contractor_cities = Contractor.city.through.objects.filter(contractor_id = contractor.id).only("city_id")
  #   contractor.cities = contractor_cities


  data = Contractor.objects.raw('SELECT hc.id, hc.name, hc.phone, hc.email, hcity.name FROM handy_contractor as hc LEFT JOIN handy_contractor_city as hcc ON hcc.contractor_id = hc.id LEFT JOIN handy_city as hcity ON hcc.city_id = hcity.id;')

  context={
    "data": data
  }

  return render(request, 'index.html', context)

def contact(request):

  return render(request, 'contact.html')