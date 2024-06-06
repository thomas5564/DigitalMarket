from django.urls import path
from .views import Dashboard
app_name="dashboard"


urlpatterns=[path('Dashboard', Dashboard, name="dash"), ]

# from django.urls import path
# from .views import SignUp,contacts,index,logout_view,login_view
# from django.contrib.auth import views as auth_views
# from .forms import LoginForm
# app_name="core"

# urlpatterns=[path("SignUp",SignUp,name="SignUp"),
#             path('contacts',contacts, name="contacts"),
#             path('', index, name="index"),
#             path('login/', login_view, name="login"), 
#             path('logout/', logout_view, name="logout"), ]