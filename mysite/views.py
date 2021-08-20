from django.shortcuts import render
import json, requests
from .models import fact
from random import randint
import pyrebase

config = {
    'apiKey': "AIzaSyBOzjInDWbg3t49n67ZExi_W02QevFAIIY",
    'authDomain': "nutrynow-e96d3.firebaseapp.com",
    'databaseURL': "https://nutrynow-e96d3.firebaseio.com",
    'projectId': "nutrynow-e96d3",
    'storageBucket': "",
    'messagingSenderId': "903955632820",
    'appId': "1:903955632820:web:89803d12c9808447"
  }
#Initialize Firebase
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()



def home(request):
    a = randint(0, 76)
    b = randint(0, 76)
    c = randint(0, 76)
    x = fact.objects.all()[a]
    y = fact.objects.all()[b]
    z = fact.objects.all()[c]
    context = {'fact1': x, 'fact2': y, 'fact3': z}
    return render(request, 'mysite/home.html', context)


def login(request):
    return render(request, 'mySite/login.html')


def about(request):
    return render(request, 'mySite/about.html')


def feature(request):
    return render(request, 'mySite/feature.html')


def signup(request):

    return render(request, 'mySite/signup.html')

def postlogin(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    print('this=',email)

    user = auth.sign_in_with_email_and_password(email, passw)
    return render(request, 'mysite/home.html', {'e':email })


def nutritionbook(request, *args, **kwargs):
    if request.method == 'POST':
        foodname = request.POST.get('fname')
        r = requests.get(
            'https://api.nutritionix.com/v1_1/search/' + foodname + '?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=2c7d3f6e&appKey=1df3d4f8744c14326890d336dccab128')
        json_data1 = json.loads(r.text)
        items = json_data1.get("hits")

        """"for i in items:
            a = i.get("fields").get("item_name")
            b = i.get("fields").get("nf_calories")
            queryset.update({a : b})
            item_id = i.get("fields").get("item_id")"""

        context = {'object_list': items}
        return render(request, 'mysite/nutritionbook.html/', context)
    else:
        return render(request, 'mysite/nutritionbook.html/')


def food(request, item_id):
    r = requests.get(
        'https://api.nutritionix.com/v1_1/item?id=' + item_id + '&appId=2c7d3f6e&appKey=1df3d4f8744c14326890d336dccab128')
    item = json.loads(r.text)
    context = {'item': item}
    return render(request, 'mysite/food.html', context)


def calci(request):
    return render(request, 'mySite/calci.html')


def bmi(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        height = height / 100
        bmi = float(weight / (height * height))
        age = request.POST.get('age')
        gender = request.POST.get('Gender')
        if gender == 'male':
            bmi = bmi * 1
        if gender == 'female':
            bmi = float(bmi * 0.8)
            print(bmi)
        w1 = 18.5 * (height * height)
        w2 = 24.9 * (height * height)

        context = {'bmi': bmi, 'w1': w1, 'w2': w2}
        return render(request, 'mysite/bmi.html', context)
    else:
        return render(request, 'mysite/bmi.html')


def bai(request):
    if request.method == 'POST':
        hip = float(request.POST.get('hip'))
        height = float(request.POST.get('height')) / 100
        bai = (hip / (height) ** 1.5) - 18
        bai = round(bai, 2)
        context = {'bai': bai}
        return render(request, 'mysite/bai.html', context)
    else:
        return render(request, 'mysite/bai.html')


def whr(request):
    if request.method == 'POST':
        waist = float(request.POST.get('waist'))
        hip = float(request.POST.get('hip'))
        whr = waist / hip
        gender = request.POST.get('Gender')
        context = {'whr': whr, 'gender': gender}
        print(whr)
        return render(request, 'mysite/whr.html', context)

    else:
        return render(request, 'mysite/whr.html')


def bmr(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')

        if gender == 'male':
            bmr = 66.47 + (13.7 * weight) + (5 * height) - (6.8 * age)
        elif gender == 'female':
            bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        context = {'bmr': bmr}
        return render(request, 'mysite/bmr.html', context)
    else:
        return render(request, 'mysite/bmr.html')


def macro(request):
    if request.method == 'POST':
        calorie = float(request.POST.get('calorie'))
        goal = request.POST.get('goal')
        if goal == 'fat':
            p = (40 / 100) * calorie
            c = (25 / 100) * calorie
            f = (35 / 100) * calorie
        elif goal == 'main':
            p = (30 / 100) * calorie
            c = (40 / 100) * calorie
            f = (30 / 100) * calorie
        elif goal == 'bulk':
            p = (30 / 100) * calorie
            c = (50 / 100) * calorie
            f = (20 / 100) * calorie
        context = {'p': p, 'c': c, 'f': f}
        return render(request, 'mysite/macro.html', context)
    else:
        return render(request, 'mysite/macro.html')


