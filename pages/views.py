from django.shortcuts import render, get_object_or_404, redirect
from groups.models import Group, Invitation
from groups.forms import InvitationForm

# Existing views
def home_view(request):
    return render(request, "pages/home.html")

def group_view(request):
    return render(request, "pages/groups.html")

def event_view(request):
    return render(request, "pages/events.html")

# New views
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST['name']
        group = Group.objects.create(name=group_name)
        return redirect('group_list')
    return render(request, 'create_group.html')

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
    return render(request, 'invite_user.html', {'form': form, 'group': group})

def accept_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)
    if request.user.email == invitation.email:
        invitation.accepted = True
        invitation.invited_user = request.user
        invitation.save()
        return redirect('group_detail', group_id=invitation.group.id)
    return render(request, 'accept_invitation.html', {'invitation': invitation})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    events = Event.objects.filter(group=group)  
    return render(request, 'group_detail.html', {'group': group, 'events': events})
