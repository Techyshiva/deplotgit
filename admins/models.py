from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# Portfolio
class Portfolio(models.Model):

    CATEGORY_CHOICES = [
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate'),
        ('social', 'Social'),
        ('custom', 'Custom'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    custom_category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.category == 'custom' and not self.custom_category:
            raise ValidationError("Custom category is required.")

        if self.category != 'custom' and self.custom_category:
            raise ValidationError("Do not fill custom category unless category is Custom.")

    def get_display_category(self):
        if self.category == 'custom':
            return self.custom_category
        return dict(self.CATEGORY_CHOICES).get(self.category)

    def __str__(self):
        return self.title
    
    
# Gallery

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    alt_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alt_text if self.alt_text else "Gallery Image"
    
# About 

class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    image = models.ImageField(upload_to='team/')
    linkedin_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    time_place = models.CharField(max_length=255, help_text="e.g. Full-time • Remote")
    experience = models.CharField(max_length=100, help_text="e.g. 3+ years experience")
    created_at = models.DateTimeField(auto_now_add=True)
    
class FeaturedEvent(models.Model):

    CATEGORY_CHOICES = [
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate'),
        ('social', 'Social'),
        ('custom', 'Custom'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    custom_category = models.CharField(max_length=100, blank=True, null=True)

    guests = models.IntegerField()
    event_date = models.DateField()

    image = models.ImageField(upload_to='featured_events/')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_display_category(self):
        if self.category == "custom" and self.custom_category:
            return self.custom_category
        return dict(self.CATEGORY_CHOICES).get(self.category)

    def __str__(self):
        return self.title
    
    
class Facility(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=100, help_text="Ionicons name (e.g., bulb-outline)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return self.question
    
class Term(models.Model):
    title = models.CharField(max_length=255) # e.g., 1. Agreement to Terms
    content = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Set order: 1, 2, 3...")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255) # e.g., 1. Information We Collect
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
        
# Testimonial
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    stars = models.PositiveSmallIntegerField(default=5)  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
