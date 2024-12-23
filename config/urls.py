"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from pages.views import home_view, group_view, event_view
from groups.views import create_group, invite_user, accept_invitation, group_list, group_detail
from accounts.views import UserLoginView, UserSignupView, log_user_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
    path('', UserLoginView.as_view(), name='root_login'),
    path('groups/', group_list, name='group_list'),  
    path('groups/create/', create_group, name='create_group'),  
    path('group/<int:group_id>/', group_detail, name='group_detail'),  
    path('group/<int:group_id>/invite/', invite_user, name='invite_user'), 
    path('accept-invitation/<int:invitation_id>/', accept_invitation, name='accept_invitation'), 
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('groups/', include('groups.urls')),
]

