from django.db import models
from django.utils import timezone



from django.db import models

class SpiceCollection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to="spices/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






class Flavor(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Optional description
    image = models.ImageField(upload_to='flavors/')  # Uploaded images saved here

    def __str__(self):
        return self.title
    


class Receipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    hour = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)

    def __str__(self):
        return self.title
    
from django.db import models

class Spice(models.Model):
    title = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='spices/', blank=True, null=True)

    def __str__(self):
        return self.title





from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pairing(models.Model):
    vegan = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    aroma = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    categories = models.CharField(max_length=255)  # comma-separated
    image = models.ImageField(upload_to='pairings/', blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models

class Product(models.Model):
  
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255, blank=True)  # e.g., Premium Grade
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    rating = models.FloatField(default=4.5)  # Example rating
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='testimonials/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
from django.db import models
# app/models.py
from django.db import models

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    help_type = models.CharField(max_length=50)
    message = models.TextField()
    agree_terms = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



class Story(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='stories/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(null=True,blank=True,default=0)


    def __str__(self):
        return self.question
    
class Blog(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='stories/', blank=True, null=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid
from django.utils import timezone

class SecurityGuard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    guard_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    shift = models.CharField(max_length=50, choices=[
        ('morning', 'Morning (6AM-2PM)'),
        ('afternoon', 'Afternoon (2PM-10PM)'),
        ('night', 'Night (10PM-6AM)'),
    ])
    gate = models.CharField(max_length=50, default='Main Gate')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.guard_id}"

class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    floor = models.CharField(max_length=20, blank=True)
    room = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.department}"

class Visitor(models.Model):
    VISITOR_TYPES = [
        ('guest', 'Guest'),
        ('contractor', 'Contractor/Vendor'),
        ('delivery', 'Delivery Person'),
        ('interview', 'Interview Candidate'),
        ('emergency', 'Emergency Services'),
        ('other', 'Other'),
    ]
    
    ID_TYPES = [
        ('driving_license', 'Driving License'),
        ('passport', 'Passport'),
        ('company_id', 'Company ID'),
        ('aadhar', 'Aadhar Card'),
        ('voter_id', 'Voter ID'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Visitor Information
    visitor_id = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])
    company = models.CharField(max_length=100)
    visitor_type = models.CharField(max_length=20, choices=VISITOR_TYPES, default='guest')
    
    # Photo and ID
    photo = models.ImageField(upload_to='visitor_photos/', blank=True, null=True)
    id_type = models.CharField(max_length=20, choices=ID_TYPES)
    id_number = models.CharField(max_length=100)
    id_photo = models.ImageField(upload_to='id_photos/', blank=True, null=True)
    
    # Visit Details
    host = models.ForeignKey(Host, on_delete=models.PROTECT, related_name='visitors')
    purpose = models.CharField(max_length=200)
    meeting_location = models.CharField(max_length=100, blank=True)
    expected_duration = models.IntegerField(help_text="Duration in minutes", default=60)
    
    # Check-in/Check-out
    check_in_time = models.DateTimeField(default=timezone.now)
    check_out_time = models.DateTimeField(blank=True, null=True)
    checked_in_by = models.ForeignKey(SecurityGuard, on_delete=models.SET_NULL, null=True, related_name='checkins')
    checked_out_by = models.ForeignKey(SecurityGuard, on_delete=models.SET_NULL, null=True, blank=True, related_name='checkouts')
    
    # Security Information
    vehicle_number = models.CharField(max_length=20, blank=True)
    emergency_contact = models.CharField(max_length=200, blank=True)
    items_brought = models.JSONField(default=list, blank=True)  # Stores list of items
    security_notes = models.TextField(blank=True)
    signature = models.TextField(blank=True)  # Store signature as base64 or SVG
    
    # Status and Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='checked_in')
    badge_number = models.CharField(max_length=20, blank=True)
    is_blacklisted = models.BooleanField(default=False)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-check_in_time']
        indexes = [
            models.Index(fields=['visitor_id']),
            models.Index(fields=['check_in_time']),
            models.Index(fields=['status']),
            models.Index(fields=['host']),
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def duration(self):
        if self.check_out_time:
            duration = self.check_out_time - self.check_in_time
            minutes = duration.total_seconds() / 60
            return f"{int(minutes)} minutes"
        return "Still checked in"
    
    def is_overdue(self):
        if self.status == 'checked_in':
            expected_end = self.check_in_time + timezone.timedelta(minutes=self.expected_duration)
            return timezone.now() > expected_end
        return False
    
    def save(self, *args, **kwargs):
        if not self.visitor_id:
            # Generate visitor ID: VIS-YYYYMMDD-XXXX
            date_str = timezone.now().strftime('%Y%m%d')
            last_visitor = Visitor.objects.filter(
                check_in_time__date=timezone.now().date()
            ).count()
            self.visitor_id = f"VIS-{date_str}-{last_visitor + 1:04d}"
        
        if not self.badge_number:
            # Generate badge number
            import random
            self.badge_number = f"BG{random.randint(1000, 9999)}"
        
        # Auto-update status if overdue
        if self.status == 'checked_in' and self.is_overdue():
            self.status = 'overdue'
        
        super().save(*args, **kwargs)

class VisitorLog(models.Model):
    ACTION_CHOICES = [
        ('check_in', 'Check In'),
        ('check_out', 'Check Out'),
        ('photo_captured', 'Photo Captured'),
        ('id_verified', 'ID Verified'),
        ('host_notified', 'Host Notified'),
        ('badge_printed', 'Badge Printed'),
        ('status_changed', 'Status Changed'),
    ]
    
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    performed_by = models.ForeignKey(SecurityGuard, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.visitor} - {self.action} at {self.timestamp}"

class Blacklist(models.Model):
    REASON_CHOICES = [
        ('security_breach', 'Security Breach'),
        ('unauthorized_access', 'Unauthorized Access'),
        ('theft', 'Theft'),
        ('violence', 'Violence/Threat'),
        ('fraud', 'Fraudulent Activity'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    id_type = models.CharField(max_length=20, choices=Visitor.ID_TYPES)
    id_number = models.CharField(max_length=100)
    reason = models.CharField(max_length=50, choices=REASON_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='blacklist_photos/', blank=True, null=True)
    added_by = models.ForeignKey(SecurityGuard, on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.id_number}"

class VisitorSettings(models.Model):
    setting_key = models.CharField(max_length=100, unique=True)
    setting_value = models.TextField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.setting_key