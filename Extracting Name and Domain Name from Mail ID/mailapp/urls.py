from django.urls import path
from.import views

urlpatterns = [
    path('',views.mail,name='index-page'),
    path('result',views.result)
]

