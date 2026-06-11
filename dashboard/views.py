from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Tournament, GalleryImage, TeamMember, ContactMessage
from .forms import TournamentForm, GalleryImageForm, TeamMemberForm


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/index.html')


# ---------------------------------------------------------------------------
# Tournaments
# ---------------------------------------------------------------------------
def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'dashboard/tournament_list.html', {
        'tournaments': tournaments,
    })


def tournament_add(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save()
            messages.success(request, f'Tournament "{tournament.name}" was created successfully.')
            return redirect('tournament_list')
    else:
        form = TournamentForm()
    return render(request, 'dashboard/tournament_add.html', {
        'form': form,
        'page_title': 'Add Tournament',
        'action_label': 'Add',
        'submit_label': 'Save Tournament',
    })


def tournament_edit(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tournament "{tournament.name}" was updated successfully.')
            return redirect('tournament_list')
    else:
        form = TournamentForm(instance=tournament)
    return render(request, 'dashboard/tournament_add.html', {
        'form': form,
        'page_title': 'Edit Tournament',
        'action_label': 'Edit',
        'submit_label': 'Update Tournament',
    })


@require_POST
def tournament_toggle(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    tournament.is_active = not tournament.is_active
    tournament.save(update_fields=['is_active'])
    state = 'activated' if tournament.is_active else 'deactivated'
    messages.success(request, f'Tournament "{tournament.name}" was {state}.')
    return redirect('tournament_list')


@require_POST
def tournament_delete(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    name = tournament.name
    tournament.delete()
    messages.success(request, f'Tournament "{name}" was deleted.')
    return redirect('tournament_list')


# ---------------------------------------------------------------------------
# Gallery
# ---------------------------------------------------------------------------
def gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'dashboard/gallery_list.html', {
        'images': images,
    })


def gallery_add(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            messages.success(request, f'Gallery image "{image.title}" was uploaded successfully.')
            return redirect('gallery_list')
    else:
        form = GalleryImageForm()
    return render(request, 'dashboard/gallery_add.html', {
        'form': form,
        'page_title': 'Add Gallery Image',
        'action_label': 'Add',
        'submit_label': 'Upload Image',
    })


def gallery_edit(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, f'Gallery image "{image.title}" was updated successfully.')
            return redirect('gallery_list')
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'dashboard/gallery_add.html', {
        'form': form,
        'page_title': 'Edit Gallery Image',
        'action_label': 'Edit',
        'submit_label': 'Update Image',
        'instance': image,
    })


@require_POST
def gallery_toggle(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    image.is_active = not image.is_active
    image.save(update_fields=['is_active'])
    state = 'activated' if image.is_active else 'deactivated'
    messages.success(request, f'Gallery image "{image.title}" was {state}.')
    return redirect('gallery_list')


@require_POST
def gallery_delete(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    title = image.title
    image.delete()
    messages.success(request, f'Gallery image "{title}" was deleted.')
    return redirect('gallery_list')


# ---------------------------------------------------------------------------
# Team members
# ---------------------------------------------------------------------------
def team_list(request):
    members = TeamMember.objects.all()
    return render(request, 'dashboard/team_list.html', {
        'members': members,
    })


def team_add(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            messages.success(request, f'Team member "{member.name}" was added successfully.')
            return redirect('team_list')
    else:
        form = TeamMemberForm()
    return render(request, 'dashboard/team_add.html', {
        'form': form,
        'page_title': 'Add Team Member',
        'action_label': 'Add',
        'submit_label': 'Save Member',
    })


def team_edit(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, f'Team member "{member.name}" was updated successfully.')
            return redirect('team_list')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'dashboard/team_add.html', {
        'form': form,
        'page_title': 'Edit Team Member',
        'action_label': 'Edit',
        'submit_label': 'Update Member',
        'instance': member,
    })


@require_POST
def team_toggle(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    member.is_active = not member.is_active
    member.save(update_fields=['is_active'])
    state = 'activated' if member.is_active else 'deactivated'
    messages.success(request, f'Team member "{member.name}" was {state}.')
    return redirect('team_list')


@require_POST
def team_delete(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    name = member.name
    member.delete()
    messages.success(request, f'Team member "{name}" was deleted.')
    return redirect('team_list')


# ---------------------------------------------------------------------------
# Contact messages
# ---------------------------------------------------------------------------
def contact_list(request):
    status = request.GET.get('status', 'all')
    all_messages = ContactMessage.objects.all()
    if status == 'unread':
        contact_messages = all_messages.filter(is_read=False)
    elif status == 'read':
        contact_messages = all_messages.filter(is_read=True)
    else:
        status = 'all'
        contact_messages = all_messages
    return render(request, 'dashboard/contact_list.html', {
        'contact_messages': contact_messages,
        'status': status,
        'total_count': all_messages.count(),
        'unread_count': all_messages.filter(is_read=False).count(),
        'read_count': all_messages.filter(is_read=True).count(),
    })


@require_POST
def contact_toggle_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_read = not msg.is_read
    msg.save(update_fields=['is_read'])
    return redirect('contact_list')


@require_POST
def contact_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    messages.success(request, 'Message deleted.')
    return redirect('contact_list')
