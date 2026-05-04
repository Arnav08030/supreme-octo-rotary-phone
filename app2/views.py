from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from django.http import JsonResponse
from .models import temp2, states, districts,country,passwords
from django.core.paginator import Paginator


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        passw= request.POST.get('password')
        try:
            models.temp2.objects.get(username=user,password=passw)
            user_data=models.temp2.objects.get(username=user,password=passw)
            request.session['user_id']=user_data.id
            return redirect('data')
        except models.temp2.DoesNotExist:
            error='Invalid Username or Password'
            return render(request, 'login.html', {'errormessage': error})
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        name= request.POST.get('name')
        email= request.POST.get('email')
        mobile= request.POST.get('mobile')
        state= request.POST.get('state')
        district= request.POST.get('district')
        country= request.POST.get('country')
        gender= request.POST.get('gender')
        language=request.POST.get('language')
        entry=models.temp2(username=username,password=password,name=name,email=email,mobile=mobile,state=state,district=district,country=country,gender=gender,language=language)
        entry.save()
        user_data=models.temp2.objects.get(username=entry.username,password=entry.password)
        request.session['user_id']=user_data.id
        return redirect('data')
    else:
        entries=temp2()
        
        return render(request,'register.html',{'entry':entries})
def data(request):
    if 'user_id' in request.session:
        user=request.session['user_id']
        user_data=models.temp2.objects.get(id=user)
        user_passwords=passwords.objects.filter(user_id=user) 
        paginator = Paginator(user_passwords, 10)
        page_number = request.GET.get('page')
        password_page = paginator.get_page(page_number)
        context={
            'entry':user_data,
            'password':password_page,
            'page_number':page_number
        }
        return render(request,'data.html',context)           
    else:
        return redirect('login')

def update(request):
    if 'user_id' in request.session:
        user_id=request.session['user_id']
        user_data=models.temp2.objects.get(id=user_id)
        
        if request.method == 'POST':
            user_data.username = request.POST.get('username')
            user_data.password = request.POST.get('password')
            user_data.name = request.POST.get('name')
            user_data.email = request.POST.get('email')
            user_data.mobile = request.POST.get('mobile')
            user_data.state = request.POST.get('state')
            user_data.district = request.POST.get('district')
            user_data.country = request.POST.get('country')
            user_data.gender = request.POST.get('gender')
            user_data.language = request.POST.get('language')
            user_data.save()
            return redirect('data')
        else:
            entries=temp2()
            return render(request,'update.html',{'user_data':user_data})
    else:
        return redirect('login')

def get_states(request):
    country_name= request.GET.get('country')
    country_id=country.objects.get(country=country_name)
    
   
    
    state_list= list(states.objects.filter(country=country_id.id).values_list('state', flat=True))
    

    
    return JsonResponse({'states':state_list})
def get_districts(request):
    state_name= request.GET.get('state')
    
    state_id=states.objects.get(state=state_name)
    district_list= list(districts.objects.filter(state=state_id.id).values_list('district', flat=True))
    
    return JsonResponse({'districts':district_list})

def input_passwords(request):
    if 'user_id' in request.session:
        user_id=request.session['user_id']
        user_data=models.temp2.objects.get(id=user_id)  

        if request.method=='POST':     
            website=request.POST.get('website')
            username=request.POST.get('username')
            password=request.POST.get('password')
            record=passwords(user_id=user_data,website=website,username=username,password=password)
            record.save()
            return redirect('data')
        else:
            return render(request,'input_passwords.html')
