from django.db.models.sql.datastructures import Join
from django.http import HttpResponse
from django.shortcuts import render
from handy.models import Contractor, City
from django.db.models.functions import Concat
from django.db.models import Aggregate, CharField, Value
from django.db import connection
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import redirect

class Card:
  name: str
  phone: str
  email: str
  cities = []
  
  def __init__(self,id,name, phone, email, cities, image, occupation):
    
    self.id = id
    self.name = name
    self.phone = phone
    self.email = email
    self.cities = cities
    self.image = image
    self.occupation = occupation

def dynamic_lookup_view(request,ID):
  card = None

  if request.user.is_authenticated:
    is_user = True
  else:
    is_user= False

  if (is_user):
    print("thats a user")
    contractor = Contractor.objects.get(id = ID)
    
    contractor_city = Contractor.city.through.objects.only("city_id").filter(contractor_id=ID)
      
    city_ids = []
    for c in contractor_city:
      city_ids.append(c.city_id)

    all_cities=[]
    for c in city_ids:
      all_cities.append((City.objects.only("name").get(id=c)).name)

    card = Card(contractor.id,contractor.name, contractor.email, contractor.phone, all_cities, contractor.image, None)

  context={
    "user": is_user,
    "data": card
  }

  return render(request, 'contractor_page.html', context)

def search_db(query):
  cards=dict()

  query_result = []
  queries = query.split()

  for q in queries:
    posts = Contractor.objects.filter(name__icontains=q)

    for post in posts:
      query_result.append(post)
  
  for row in query_result:
    id = row.id
    contractor_city = Contractor.city.through.objects.only("city_id").filter(contractor_id=id)
    
    city_ids = []
    for c in contractor_city:
      city_ids.append(c.city_id)

    all_cities=[]
    for c in city_ids:
      all_cities.append((City.objects.only("name").get(id=c)).name)

    cards[row.id] = Card(row.id,row.name, row.email, row.phone, all_cities, row.image, None)

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
    cards[row[0]] = Card(row[0],row[1], row[2], row[3], cities, row[4], None)

  if(query):
    context={
    "data": search_db(search)
    }

  else:
    context={
      "data": cards
    }

  return render(request, 'index.html', context)

'''
def login(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      username = request.POST['username']
      password =  request.POST['password']
      post = User.objects.filter(username=username)
      if post:
        username = request.POST['username']
        request.session['username'] = username
        return redirect("profile")
      else:
        return render(request, 'registration/login.html', {})
    return render(request, 'registration/login.html', {})
  else:
    return redirect("profile")
'''

def register(request):

  context={
    "data":None
  }

  return render(request, 'registration/registration.html', context)

'''
def profile(request):
  if request.session.has_key('username'):
    posts = request.session['username']
    query = User.objects.filter(username=posts) 
    return render(request, 'profile.html', {"query":query})
  else:
    return render(request, 'registration/login.html', {})
'''
