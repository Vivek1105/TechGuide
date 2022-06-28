from django.contrib import admin
from django.urls import path, include
from app import views


# django admin header custimization 
admin.site.site_header = "Tech Guide"
admin.site.index_title = "Welcome to Tech Guide "
admin.site.site_title = "Welcome to our Dasboard"



urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('Hackathon',views.Hackathon,name='Hackathon'),
    path('google',views.google,name='google'),
    path('amazon',views.amazon,name='amazon'),
    path('adobe',views.adobe,name='adobe'),
    path('intel',views.intel,name='intel'),
    
]
