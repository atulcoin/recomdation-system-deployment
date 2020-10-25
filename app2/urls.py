from django.urls import path
from . import views
urlpatterns = [
    path('singup',views.singup, name='singup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout' ),
    path('vidb',views.vidb,name='vidb'),
    path('form1',views.form1,name='form'),
    path('delete',views.delete,name='delete')
    
]