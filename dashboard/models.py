from django.db import models


class Tournament(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    FORMAT_CHOICES = [
        ('classical', 'Classical'),
        ('rapid', 'Rapid'),
        ('blitz', 'Blitz'),
        ('bullet', 'Bullet'),
    ]

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    game_format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='classical')
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    max_participants = models.PositiveIntegerField(default=0, help_text='0 means unlimited')
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prize_pool = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    registration_link = models.URLField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('winners', 'Winners'),
        ('championship', 'Championship'),
        ('coach', 'Coach'),
        ('goalkeepers', 'Goalkeepers'),
    ]

    title = models.CharField(max_length=200)
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE,
        related_name='gallery_images', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='winners')
    image = models.ImageField(upload_to='gallery/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.email})'


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, help_text='e.g. Grandmaster, Founder, Coach')
    photo = models.ImageField(upload_to='team/')
    jersey_number = models.CharField(max_length=10, blank=True)
    biography = models.TextField(blank=True)
    facebook = models.URLField(max_length=300, blank=True)
    twitter = models.URLField(max_length=300, blank=True)
    vimeo = models.URLField(max_length=300, blank=True)
    pinterest = models.URLField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
