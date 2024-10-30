from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Invitation, Group
from .forms import InvitationForm
from events.models import Event

def create_group(request):
    if request.method == 'POST':
        group_name = request.POST['name']
        group = Group.objects.create(name=group_name)
        return redirect('group_detail', group_id=group.id)
    return render(request, 'groups/create_group.html')

def invite_user(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.group = group
            invitation.invited_by = request.user
            invitation.save()
            
            send_mail(
                'Group Invitation',
                f'You are invited to join the group {group.name}.',
                'from@example.com',
                [invitation.email],
                fail_silently=False,
            )
            return redirect('group_detail', group_id=group.id)
    else:
        form = InvitationForm()
    return render(request, 'groups/invite_user.html', {'form': form, 'group': group})

def accept_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    if request.user.email == invitation.email:
        invitation.accepted = True
        invitation.invited_user = request.user
        invitation.save()
        return redirect('groups/group_detail', group_id=invitation.group.id)
    return render(request, 'groups/accept_invitation.html', {'invitation': invitation})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/group_list.html', {'groups': groups})

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    events = Event.objects.filter(group=group)  # Fetch events related to the group
    return render(request, 'groups/group_detail.html', {'group': group, 'events': events})
