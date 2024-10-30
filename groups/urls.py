from django.urls import path
from .views import create_group, invite_user, accept_invitation, group_list, group_detail

urlpatterns = [
    path('', group_list, name='group_list'),  
    path('create/', create_group, name='create_group'),  
    path('<int:group_id>/', group_detail, name='group_detail'),  
    path('<int:group_id>/invite/', invite_user, name='invite_user'),  
    path('accept-invitation/<int:invitation_id>/', accept_invitation, name='accept_invitation'), 
]
