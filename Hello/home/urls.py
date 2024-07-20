from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.index,name='home'), #index here is a function 
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact')
]
