from django.shortcuts import render
from . forms import contactForm

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html')

def about(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name':name, 'email':email, 'select': select})
    else:
        return render(request, './first_app/about.html')

def submit_form(request):
        return render(request, './first_app/form.html') 
    
def DjangoForm(request):
    form = contactForm()
    return render(request,'./first_app/django_form.html', {'form':form})
    