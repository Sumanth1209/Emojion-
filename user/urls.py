from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.first,name='first'),
    path('happy.html',views.happy,name='happy'),
    path('sad.html',views.sad,name='sad'),
    path('suprise.html',views.suprise,name='suprise'),
    path('fear.html',views.fear,name='fear'),
    path('angry.html',views.angry,name='angry'),
    path('confused.html',views.confused,name='confused'),
    path('index.html',views.login,name='login'),
    path('login',views.login_user,name='login_user'),
    #path('happy_value',views.happy_value,name='happy_value'),
    path('signup/', views.signup,name='signup'),
    path('profile/',views.profile, name='profile'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('source',views.source,name='source'),
    path('thankyou',views.thankyou,name='thank'),
]