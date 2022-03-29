from django.contrib import admin
from django.urls import path,include
from home.views import home
from hrhome.views import hrhome
from employee.views import index,hiit,yoga,events,recommendation
from auapp.views import user_signup,user_login,user_logout,user_np,ulogin,ulogout,ucreate,delete,cevent,devent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('',include('home.urls')),
    path("index/",index,name = "index"),
    path("hiit/",hiit,name = "hiit"),
    path("employee/",include('employee.urls')),
    path("yoga/",yoga,name = "yoga"),
    path("user_signup/",user_signup,name="user_signup"),
    path("user_login/",user_login,name="user_login"),
    path("user_logout/",user_logout,name="user_logout"),
    path("user_np/",user_np,name="user_np"),
    path("hrhome",hrhome,name="hrhome"),
    path("ulogin/" , ulogin,name="ulogin"),
    path("ulogout/" , ulogout,name="ulogout"),
    path("ucreate/",ucreate,name="ucreate"),
    path("delete/<str:id>",delete,name="delete"),
    path("cevent/",cevent,name="cevent"),
    path("devent",devent,name = "devent"),
    path("events/",events,name = "events"),
    path("recommendation/",recommendation,name="recommendation"),


]
