from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contactInformation/',views.basicDataCollector,name="contactInformation"),
     path('educationform/<int:pk>/', views.education_form_creation, name='educationform'),
  
]
