from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):

    return render(request, 'index.html')

def register(request):
    # if User.objects.filter(email = request.POST['email']):
    #     return redirect('/')

    msgs = User.objects.regValidator(request.POST)
    if msgs:
        print(msgs)
        for key,values in msgs.items():
            print("value : ",values,"key",key)
            messages.error(request, values, extra_tags = key)



        return redirect('/')
    else :
        password = request.POST['password']
        hashedpw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashedpw)
        request.session['logged_in'] = user.id
        request.session['status'] = "Registered"
        return redirect('/home')

def login(request):
    if request.POST['login_email'] == "admin@admin.com" and request.POST['login_password'] == "password":
        return redirect('/admin')

    msgs = User.objects.loginValidator(request.POST)
    if msgs:
        for key,values in msgs.items():
            print("value : ",values,"key",key)
            messages.error(request, values, extra_tags = key)

        return redirect('/')

    else:
        users = User.objects.filter(email = request.POST['login_email'])
        request.session['logged_in'] = users[0].id
        request.session['status'] = "logged in"
        return redirect('/home')

def home(request):
    if not request.session['logged_in']:
        return redirect('/')

    return render(request, 'gateway.html')

def california(request):
    return render (request, 'california.html')
def kerala(request):
    return render (request, 'kerala.html')
def freetown(request):
    return render (request, 'freetown.html')
def support(request):
    return render (request, 'support.html')
def food(request):
    return render (request, 'food.html')
def shelter(request):
    return render (request, 'shelter.html')
def organizations(request):
    return render (request, 'organizations.html')
def medical(request):
    return render (request, 'medical.html')
def technology(request):
    return render (request, 'technology.html')

def admin(request):
    disasters =  Disaster.objects.all()
    print("organizations : ", disasters[0].works_for.all())
    return render(request,"admin_home.html",{ 'disasters' : Disaster.objects.all(), 'organizations' : Organization.objects.all()})

def add_disaster(request):
    disaster = Disaster.objects.create(title = request.POST['title'], location = request.POST['location'], body = request.POST['body'] )
    print("new disaster : ", disaster)
    return redirect('/admin')

def add_ngo(request):
    org = Organization.objects.create(name = request.POST['name'], description = request.POST['description'])



    print("new organization : ", org)
    return redirect('/admin')

def link_org(request, id):
    disaster = Disaster.objects.get(id = id)
    orgs = Organization.objects.all()
    return render(request,'link_org.html', {'disaster' : disaster, 'orgs' : orgs})

def link_org_process(request,id):
    disaster = Disaster.objects.get(id = id)
    org = Organization.objects.get(id = request.POST['organization'])
    org.works_on.add(disaster)
    return redirect('/admin')

def posts_kerala(request):
    return render(request,"post_kerala.html")

def delete_cause(request,id):
    d= Disaster.objects.get(id = id)
    d.works_for.clear()
    d.delete()
    return redirect('/admin')

def rem_org(request, o_id,d_id):
    d = Disaster.objects.get(id = d_id)
    o = Organization.objects.get(id = o_id)
    d.works_for.remove(o)
    return redirect('/admin')

def logout(request):
    if not request.session['logged_in']:
        return redirect('/')
    request.session.clear()
    return redirect('/')