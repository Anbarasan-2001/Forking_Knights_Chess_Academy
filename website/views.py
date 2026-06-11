from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from dashboard.models import GalleryImage, Tournament, TeamMember, ContactMessage

# Create your views here.
def home(request):
    tournament_list = Tournament.objects.filter(is_active=True)[:6]
    members = TeamMember.objects.filter(is_active=True)
    return render(request, 'website/index.html', {
        'tournaments': tournament_list,
        'team_members': members,
    })

def about(request):
    members = TeamMember.objects.filter(is_active=True)
    return render(request, 'website/about.html', {
        'team_members': members,
    })

def gallery(request):
    images = GalleryImage.objects.filter(is_active=True).select_related('tournament')
    # Tournaments that have at least one active gallery image, newest first.
    gallery_tournaments = (
        Tournament.objects.filter(gallery_images__is_active=True)
        .distinct()
        .order_by('-start_date')
    )
    return render(request, 'website/gallery.html', {
        'gallery_images': images,
        'gallery_tournaments': gallery_tournaments,
    })

def tournaments(request):
    tournament_list = Tournament.objects.filter(is_active=True)
    return render(request, 'website/tournaments.html', {
        'tournaments': tournament_list,
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')
        messages.error(request, 'Please fill in your name, email and message.')
    return render(request, 'website/contact.html')

def team_details(request, pk=None):
    members = TeamMember.objects.filter(is_active=True)
    if pk is not None:
        member = get_object_or_404(TeamMember, pk=pk, is_active=True)
    else:
        member = members.first()
    return render(request, 'website/team_details.html', {
        'member': member,
        'members': members,
    })