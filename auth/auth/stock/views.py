from django.shortcuts import render, redirect  
from stock.forms import StockForm  
from stock.models import Stock   
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #f=form.save(commit=False)
            # if f.choice=='deo':
            #     f.deo=True
            #     #return render(request,'home.html')
            # else:
            #     f.deo=False
            #     #return render(request,'fachome.html')
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


def login(request):
    m = User.objects.get(username=request.POST['username'])
    if m.check_password(request.POST['password']):
        request.session['user_id'] = m.id
        # if request.User.choice == 'deo':
        #     request.session['user_id'] = m.id
        #     return render(request,"home.html")
        # else:
        #     request.session['user_id'] = m.id
        #     return render(request,"fachome.html")
        return render(request,"home.html")
    else:
        return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def add(request):  
    if request.method == "POST":  
        form = StockForm(request.POST)  
        if form.is_valid():  
            try:  
                f=form.save()
                f.user=request.user
                f.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StockForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    stocks = Stock.objects.filter(user=request.user)#User.objects.get(username=request.user)  
    return render(request,"show.html",{'stocks':stocks})  

def edit(request, id):  
    stock = Stock.objects.get(id=id)  
    return render(request,'edit.html', {'stock':stock})  

def update(request, id):  
    stock = Stock.objects.get(id=id)  
    form = StockForm(request.POST, instance = stock)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'stock': stock})
    
def destroy(request, id):  
    stock = Stock.objects.get(id=id)  
    stock.delete()  
    return redirect("/show")  



