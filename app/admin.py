from django.contrib import admin
from .models import (
    SpiceCollection,
    Pairing,
    Category,
    Testimonial,
    Flavor,
    Receipe,
    Spice,
    Product,
    Story,
    ContactMessage
)

# Register models without customization
admin.site.register(SpiceCollection)
admin.site.register(Pairing)
admin.site.register(Category)
admin.site.register(Flavor)
admin.site.register(Receipe)
admin.site.register(Spice)
admin.site.register(Product)
admin.site.register(Story)
admin.site.register(ContactMessage)

# Register Testimonial with customization
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')
    search_fields = ('name', 'role', 'content')
