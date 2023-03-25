"""digitalsociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from chairmanapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('change-password/', views.change_password, name='change-password'),
    path('logout/', views.logout, name='logout'),
    path('chairman_profile/', views.chairman_profile, name='chairman_profile'),    
    path('chairman_change_password/', views.chairman_change_password, name='chairman_change_password'),
    path('add-member/', views.add_member, name='add-member'),    
    path('add-notice/', views.add_notice, name='add-notice'),    
    path('view-notice/', views.view_notice, name='view-notice'),    
    path('view-notice-details/<int:pk>', views.view_notice_details, name='view-notice-details'),     
    path('all-societymembers/', views.all_societymembers, name='all-societymembers'),
    path('specific-societymember-profile/<int:pk>', views.specific_societymember_profile, name='specific-societymember-profile'),
    path('specific-chairman-profile/>', views.specific_chairman_profile, name='specific-chairman-profile'),
    path('add-event/', views.add_event, name='add-event'),
    path('view-event/', views.view_event, name='view-event'),
    path('view-event-details/<int:pk>', views.view_event_details, name='view-event-details'),     
    path('add-complaint/', views.add_complaint, name='add-complaint'),
    path('view-complaint/', views.view_complaint, name='view-complaint'),
    path('view-complaint-details/<int:pk>', views.view_complaint_details, name='view-complaint-details'),
]

