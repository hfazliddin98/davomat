from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponse
from davomat.models import Yonalish, Kurs, Team



@csrf_exempt
def kirish(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.save()
            return redirect('/')
        else:
            return redirect('/users/')

    return render(request, 'users/login.html')


@csrf_exempt
def home(request):
    
    yonalish = Yonalish.objects.all()
    kurs = Kurs.objects.all()
    try:
        if request.method == "POST":
            yonalish_id = request.POST['yonalish']
            kurs_id = request.POST['kurs']
            data = Team.objects.filter(yonalish=yonalish_id).filter(kurs=kurs_id)
        else:
            data = ''            

    except:        
        return HttpResponse('<h1>Ma`lumot topilmadi</h1>')    

    context = {
        'kurs':kurs,
        'yonalish':yonalish,
        'data':data,
    }
    return render(request, 'asosiy/home.html', context)


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('/')