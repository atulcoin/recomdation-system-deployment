from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import emp
from .models import movieId


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def vidb(request):
    data = movieId.objects.all()
    return render(request,"vdb.html",{'data':data})
    

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else :
            messages.info(request,'chuitye galat hai tera paass')
            return redirect("login")
    else:
        return render(request,'login.html')



def singup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already exists')
                return redirect('singup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('singup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user Created')
                return redirect('singup')
        else:
            messages.info(request,'password missmatch')
            return redirect('singup')

    else:
        return render(request,'sing.html')

from .forms import inputdata
def form1(request):
    con = inputdata(request.POST or None)
    savedata=request.session.get('newformdata')
    print(savedata)
    if request.method == 'POST':
        
        if con.is_valid():
            n98 = con.cleaned_data['first_name']
            data1 = con.cleaned_data['addresss']
            s981 = con.cleaned_data['salary']
            status=con.cleaned_data['status']
            emp(Name=n98,address=data1,salary=s981,status=status).save()
            msg="Data Stored Successfully"
            return render(request,"form1.html",{'msg':msg,'form':con})
    return render(request,'form1.html',{'form':con})

def delete(request):
    nisha = request.GET['id']
    emp.objects.filter(id=nisha).delete()
    return redirect('vidb')


