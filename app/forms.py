from django import forms
from .models import (
    SpiceCollection, Flavor, Receipe,
    Spice, Pairing, Product, Testimonial, ContactMessage
)

# --------------------------
# SpiceCollection Form
# --------------------------
from django import forms
from .models import SpiceCollection

class SpiceCollectionForm(forms.ModelForm):
    class Meta:
        model = SpiceCollection
        fields = ['name', 'description', 'count', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter collection name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter description'
            }),
            'count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of spices'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }


# --------------------------
# Flavor Form
# --------------------------
class FlavorForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter flavor title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# --------------------------
# Receipe Form
# --------------------------
class ReceipeForm(forms.ModelForm):
    class Meta:
        model = Receipe
        fields = ['title', 'description', 'image', 'hour', 'time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter recipe title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'hour': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter hours'}),
            'time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter minutes'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# --------------------------
# Spice Form
# --------------------------
class SpiceForm(forms.ModelForm):
    class Meta:
        model = Spice
        fields = ['title', 'quality', 'price', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter spice name'}),
            'quality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quality (e.g., Premium)'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price in ₹'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# --------------------------
# Pairing Form
# --------------------------
class PairingForm(forms.ModelForm):
    class Meta:
        model = Pairing
        fields = ['name', 'aroma', 'price', 'description', 'image', 'categories','vegan']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pairing name'}),
            'aroma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter aroma'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categories': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pairing name'}),
            'vegan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pairing name'}),
            

        }

# --------------------------
# Product Form
# --------------------------
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'grade', 'price', 'image', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.5, 'max': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# --------------------------
# Testimonial Form
# --------------------------
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'image', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
from django import forms
from django.core.validators import RegexValidator
from .models import Visitor, Host, SecurityGuard, Blacklist
from django.utils import timezone
import re

class VisitorCheckinForm(forms.ModelForm):
    # Visitor Information
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name',
            'required': 'required'
        })
    )
    
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name',
            'required': 'required'
        })
    )
    
    phone = forms.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                    message="Enter a valid phone number")],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 (555) 123-4567',
            'required': 'required'
        })
    )
    
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'visitor@example.com'
        })
    )
    
    company = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Company name',
            'required': 'required'
        })
    )
    
    visitor_type = forms.ChoiceField(
        choices=Visitor.VISITOR_TYPES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': 'required'
        })
    )
    
    # Photo upload
    photo = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
            'capture': 'environment'
        })
    )
    
    # ID Information
    id_type = forms.ChoiceField(
        choices=Visitor.ID_TYPES,
        widget=forms.RadioSelect(attrs={
            'class': 'btn-check'
        })
    )
    
    id_number = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter ID number',
            'required': 'required'
        })
    )
    
    id_photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )
    
    # Visit Details
    host = forms.ModelChoiceField(
        queryset=Host.objects.filter(is_active=True),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': 'required'
        })
    )
    
    purpose = forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 2,
            'placeholder': 'Purpose of visit',
            'required': 'required'
        })
    )
    
    meeting_location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Conference Room A, Floor 3, etc.'
        })
    )
    
    expected_duration = forms.ChoiceField(
        choices=[
            (30, '30 minutes'),
            (60, '1 hour'),
            (120, '2 hours'),
            (240, '4 hours'),
            (480, 'Full day (8 hours)'),
            (1440, 'Multiple days'),
        ],
        initial=60,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    check_in_time = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )
    
    # Security Information
    vehicle_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'License plate number'
        })
    )
    
    emergency_contact = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name and phone number'
        })
    )
    
    # Items brought in
    ITEM_CHOICES = [
        ('laptop', 'Laptop'),
        ('camera', 'Camera'),
        ('tools', 'Tools/Equipment'),
        ('bag', 'Bag/Briefcase'),
        ('mobile', 'Mobile Phone'),
        ('documents', 'Documents/Files'),
        ('other', 'Other'),
    ]
    
    items_brought = forms.MultipleChoiceField(
        choices=ITEM_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        })
    )
    
    security_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Any special instructions or security notes...'
        })
    )
    
    signature = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )
    
    class Meta:
        model = Visitor
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'company',
            'visitor_type', 'photo', 'id_type', 'id_number', 'id_photo',
            'host', 'purpose', 'meeting_location', 'expected_duration',
            'check_in_time', 'vehicle_number', 'emergency_contact',
            'items_brought', 'security_notes', 'signature'
        ]
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Remove all non-numeric characters except plus sign
        phone = re.sub(r'[^\d+]', '', phone)
        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        # Check against blacklist
        id_number = cleaned_data.get('id_number')
        id_type = cleaned_data.get('id_type')
        
        if id_number and id_type:
            blacklisted = Blacklist.objects.filter(
                id_number=id_number,
                id_type=id_type,
                is_active=True
            ).exists()
            
            if blacklisted:
                raise forms.ValidationError(
                    "This ID is blacklisted. Please contact security supervisor."
                )
        
        return cleaned_data

class QuickCheckinForm(forms.Form):
    """Form for quick check-in using QR code or pre-registration"""
    
    qr_code = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Scan QR code or enter visitor ID'
        })
    )
    
    visitor_id = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Or enter pre-registered visitor ID'
        })
    )
    
    capture_photo = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

class VisitorCheckoutForm(forms.Form):
    visitor_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Scan badge or enter visitor ID'
        })
    )
    
    check_out_time = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )
    
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 2,
            'placeholder': 'Checkout notes...'
        })
    )

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['name', 'email', 'phone', 'department', 'floor', 'room', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class BlacklistForm(forms.ModelForm):
    class Meta:
        model = Blacklist
        fields = ['name', 'id_type', 'id_number', 'reason', 'description', 'photo', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_type': forms.Select(attrs={'class': 'form-select'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class SearchForm(forms.Form):
    SEARCH_BY_CHOICES = [
        ('name', 'Name'),
        ('company', 'Company'),
        ('phone', 'Phone'),
        ('visitor_id', 'Visitor ID'),
        ('badge_number', 'Badge Number'),
        ('host', 'Host'),
    ]
    
    search_by = forms.ChoiceField(
        choices=SEARCH_BY_CHOICES,
        initial='name',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search...'
        })
    )
    
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

class SecurityGuardLoginForm(forms.Form):
    guard_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your guard ID'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    
    gate = forms.CharField(
        max_length=50,
        initial='Main Gate',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Current gate location'
        })
    )
# --------------------------
# Contact Form
# --------------------------
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'help_type', 'message', 'agree_terms']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'help_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HELP TYPE'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here...', 'rows': 4}),
            'agree_terms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'subtitle', 'content', 'image']



