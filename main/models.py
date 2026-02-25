from django.db import models

# Create your models here.

class EventBooking(models.Model):
    # Event Details
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    event_city = models.CharField(max_length=100)
    expected_guests = models.IntegerField()
    event_budget = models.CharField(max_length=100)
    
    # Client Info
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    additional_info = models.TextField(blank=True, null=True)
    
    # Admin Data
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.event_type} ({self.event_date})"
      
      
class ContactEnquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    event_type = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    
    # Admin Data
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"