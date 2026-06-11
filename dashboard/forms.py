from django import forms
from .models import Tournament, GalleryImage, TeamMember


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = [
            'name', 'location', 'game_format', 'start_date', 'end_date',
            'start_time', 'end_time', 'max_participants', 'entry_fee',
            'prize_pool', 'status', 'registration_link', 'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter tournament name'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter location'}),
            'game_format': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'max_participants': forms.NumberInput(attrs={
                'class': 'form-control', 'min': 0, 'placeholder': '0 for unlimited'}),
            'entry_fee': forms.NumberInput(attrs={
                'class': 'form-control', 'min': 0, 'step': '0.01', 'placeholder': '0.00'}),
            'prize_pool': forms.NumberInput(attrs={
                'class': 'form-control', 'min': 0, 'step': '0.01', 'placeholder': '0.00'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'registration_link': forms.URLInput(attrs={
                'class': 'form-control', 'placeholder': 'https://example.com/register'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4, 'placeholder': 'Enter a short description'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and end_date < start_date:
            self.add_error('end_date', 'End date cannot be earlier than the start date.')
        return cleaned_data


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'tournament', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter image title'}),
            'tournament': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tournament'].queryset = Tournament.objects.all()
        self.fields['tournament'].empty_label = 'Select a tournament'
        # When editing an existing image, allow keeping the current file.
        if self.instance and self.instance.pk:
            self.fields['image'].required = False


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = [
            'name', 'role', 'photo', 'jersey_number', 'biography',
            'facebook', 'twitter', 'vimeo', 'pinterest',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Grandmaster'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'jersey_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 07'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Short biography'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/...'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
            'vimeo': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://vimeo.com/...'}),
            'pinterest': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://pinterest.com/...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # When editing, keep the existing photo if no new one is uploaded.
        if self.instance and self.instance.pk:
            self.fields['photo'].required = False
