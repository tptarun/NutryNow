from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('about', views.about, name="about"),
    path('feature', views.feature, name="feature"),
    path('signup', views.signup, name="signup"),
    path('bmi', views.bmi, name="bmi"),
    path('bai', views.bai, name="bai"),
    path('whr', views.whr, name="whr"),
    path('bmr', views.bmr, name="bmr"),
    path('calci', views.calci, name="calci"),
    path('macro', views.macro, name="macro"),
    path('nutritionbook', views.nutritionbook, name="nutritionbook"),
    path('food/<item_id>', views.food, name="food"),
    path('postlogin', views.postlogin, name="postlogin"),


]
