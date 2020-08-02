from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm

from handy import views as handy_views
from .forms import UserRegisterForm

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("SOMETHING WORKED")
            return redirect('index')
    else:
        form = UserRegisterForm()

    context={
        "form": form
    }

    return render(request, 'registration/registration.html', context)