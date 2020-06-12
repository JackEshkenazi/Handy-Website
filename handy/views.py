from django.db.models.sql.datastructures import Join
from django.http import HttpResponse
from django.shortcuts import render
from handy.models import Contractor, City
from django.db.models.functions import Concat
from django.db.models import Aggregate, CharField, Value
from django.db import connection
from django.db.models import Q

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



def search_db(query):
  print("HEEERE")
  cards=dict()

  query_result = []
  queries = query.split()

  for q in queries:
    posts = Contractor.objects.filter(
      Q(name=q) |
      Q(email=q)
    ).distinct()
    print(posts)

    for post in posts:
      query_result.append(post)
  
  for row in query_result:
    print(row)
    try:
      cities = row[4].split(",")
    except:
      cities = []
    cards[row[0]] = Card(row[1], row[2], row[3], cities)


  return cards

def index(request):
  query = ""
  if request.GET:
    query = request.GET['q']
    search = str(query)


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

  if(query):
    context={
    "data": search_db(search)
    }

  else:
    context={
      "data": cards
    }

  return render(request, 'index.html', context)


