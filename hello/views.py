from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request, 'success.html', {'username': username})
    
    return render(request, 'login.html', {'form': form})

