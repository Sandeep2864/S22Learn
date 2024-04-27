from django.urls import path
from .views import *

urlpatterns = [
    path('home/', homepage, name="home"),
    path('login/',login_view,name="login"),
    path('signup/',signup,name="signup"),
    path('reg/',registration,name="registration"),
    path('dashboard/apply', apply,name="apply"),
    path('dashboard/practice',practice,name="practice"),
    path('dashboard/profile',profile,name="profile"),
    path('dashboard/jobs',jobs,name="jobs"),
    path('',intro,name="intro"),
    path('admin/',admin,name="admin"),
    path('recruiter/',recruiter,name="recruiter"),
    path('recruiter/dashboard',recru_dash,name="recru_dash"),
]
