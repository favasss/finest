from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages, auth

from finalapp.forms import MypcForm
from finalapp.models import Mypc

name='finalapp'
# Create your views here.
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email= email,password=password)


                user.save();
                return redirect('/login.html')

        else:
               messages.info(request,"password not matching")
               return redirect('/')


        return redirect('/')

    return render(request,"register.html")


def home(request):
    user = request.user
    if user.is_authenticated:
        username = user.username
    else:
        username = None
    context = {
        'username': username,
        'mypc_list': Mypc.objects.all(),
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('/home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login.html')
    else:
        return render(request, 'login.html')


def browse(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        mypc=Mypc(name=name,desc=desc,year=year,img=img)
        mypc.save()
        return redirect('/home')
    return render(request,'browse.html')

def detail(request,mypc_id):
    mypc=Mypc.objects.get(id=mypc_id)
    return render(request,"detail.html",{'mypc':mypc})


def update(request,id):
    mypc=Mypc.objects.get(id=id)
    form=MypcForm(request.POST or None, request.FILES,instance=mypc)
    if form.is_valid():
        form.save()
        return redirect('/home')
    return render(request,'edit.html',{'form':form,'mypc':mypc})


def delete(request,id):
    if request.method=='POST':
        mypc=Mypc.objects.get(id=id)
        mypc.delete()
        return redirect('/home')
    return render(request,'delete.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
