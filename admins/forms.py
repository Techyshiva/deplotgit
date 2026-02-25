from django import forms
from .models import Portfolio, Gallery, TeamMember , JobOpening,Facility , Blog,FAQ,Term,PrivacyPolicy, FeaturedEvent, Testimonial

class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ['title', 'category', 'custom_category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field', 'id': 'category-field'}),
            'custom_category': forms.TextInput(attrs={'class': 'input-field', 'id': 'custom-category-field'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        custom_category = cleaned_data.get("custom_category")

        if category == "custom":
            if not custom_category:
                self.add_error('custom_category', "Please enter custom category.")
        else:
            # Automatically clear custom_category if not needed
            cleaned_data["custom_category"] = None

        return cleaned_data
    
    

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['image', 'alt_text']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'alt_text': forms.TextInput(attrs={'class': 'input-field'}),
        }
        
        
 

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'image', 'linkedin_url', 'is_active']
        
 

class JobOpeningForm(forms.ModelForm):
    class Meta:
        model = JobOpening
        fields = ['title', 'time_place', 'experience']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Job Title'}),
            'time_place': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Full-time • Remote'}),
            'experience': forms.TextInput(attrs={'class': 'input-field', 'placeholder': '3+ years experience'}),
        }
        
        
class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['title', 'description', 'icon_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Stage & Lighting'}),
            'description': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Professional stage design...'}),
            'icon_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'bulb-outline'}),
        }
        
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'description', 'date']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Blog Title'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Short description...', 'rows': 3}),
            'date': forms.DateInput(attrs={'class': 'input-field', 'type': 'date'}),
        }
    
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'e.g., How far in advance should I book?'}),
            'answer': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Provide a detailed answer...', 'rows': 4}),
        }
        
class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'e.g., 1. Agreement to Terms'}),
            'content': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Detailed legal text...', 'rows': 5}),
            'order': forms.NumberInput(attrs={'class': 'input-field'}),
        }
class PrivacyPolicyForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicy
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'e.g., 1. Information We Collect'}),
            'content': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Policy details...', 'rows': 5}),
            'order': forms.NumberInput(attrs={'class': 'input-field'}),
        }
class FeaturedEventForm(forms.ModelForm):

    class Meta:
        model = FeaturedEvent
        fields = [
            'title',
            'category',
            'custom_category',
            'guests',
            'event_date',
            'image',
            'is_active'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'category': forms.Select(attrs={'class': 'input-field'}),
            'custom_category': forms.TextInput(attrs={'class': 'input-field'}),
            'guests': forms.NumberInput(attrs={'class': 'input-field'}),
            'event_date': forms.DateInput(attrs={
                'class': 'input-field',
                'type': 'date'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'checkbox-field'}),
        }
        

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'text', 'image', 'stars']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field'}),
            'role': forms.TextInput(attrs={'class': 'input-field'}),
            'text': forms.Textarea(attrs={'class': 'input-field', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'stars': forms.NumberInput(attrs={'class': 'input-field', 'min': 1, 'max': 5}),
        }