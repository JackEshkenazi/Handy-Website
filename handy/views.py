from django.db.models.sql.datastructures import Join
from django.http import HttpResponse
from django.shortcuts import render
from handy.models import Contractor, City
from django.db.models.functions import Concat
from django.db.models import Aggregate, CharField, Value
from django.db import connection

class Card:
  name: str
  phone: str
  email: str
  cities = []
  def __init__(self, name, phone, email, cities):
    self.name = name
    self.phone = phone
    self.email = email
    self.cities = cities


def index(request):
  cursor = connection.cursor()
  cursor.execute('''SELECT hc.id AS id, hc.name, hc.phone, hc.email,  group_concat(hcity.name, ',') AS cities 
    FROM handy_contractor AS hc 
    LEFT JOIN handy_contractor_city as hcc 
    ON hcc.contractor_id = hc.id 
    LEFT JOIN handy_city AS hcity ON
    hcc.city_id = hcity.id GROUP BY hc.name, hc.phone, hc.email''')
  cards = dict()
  query_result = cursor.fetchall()
  for row in query_result:
    try:
      cities = row[4].split(",")
    except:
      cities = []
    cards[row[0]] = Card(row[1], row[2], row[3], cities)

  print(cards)

  context={
    "data": cards
  }

  return render(request, 'index.html', context)

def contact(request):

  return render(request, 'contact.html')