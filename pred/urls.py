from django.urls import path
from . import views

#URLCONF
urlpatterns=[
    path('',views.predict,name="predict"),
    path('result/',views.result,name="result"),
]