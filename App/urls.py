from django.urls import path
from .import views


urlpatterns=[ 
    path('event/',views.Event_list),
    path('details/<int:pk>',views.Event_Details)
]