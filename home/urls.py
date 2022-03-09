from turtle import home
from unicodedata import name
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginuser, name="login"),
    path('logout',views.logoutuser, name="logout"),
    path('signup',views.signup,name="signup"),
]
#<body>
#   welcome {{request.user}}
#   <p> this is index page</p>
#   <a href="/logout"> logout </a>
#</body>