from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views
from django.contrib import admin
from django.urls import path, include  # include if you have app urls



urlpatterns = [
    # Frontend
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('add/', views.add_spice_collection, name='add_spice_collection'),
    # SpiceCollection CRUD
    path('spice-collections/', views.add_spice_collection, name='add_spice_collection'),
    path('spice-collections/edit/<int:pk>/', views.edit_spice_collection, name='edit_spice_collection'),
    path('spice-collections/delete/<int:pk>/', views.delete_spice_collection, name='delete_spice_collection'),
   
  

    # Flavor CRUD
    path('flavors/', views.shop_by_flavour, name='shop_by_flavour'),
    path('flavors/edit/<int:pk>/', views.edit_flavor, name='edit_flavor'),
    path('flavors/delete/<int:pk>/', views.delete_flavor, name='delete_flavor'),

    # Recipe CRUD
    path('recipes/', views.receipe, name='receipe'),
    path('recipes/edit/<int:pk>/', views.edit_receipe, name='edit_receipe'),
    path('recipes/delete/<int:pk>/', views.delete_receipe, name='delete_receipe'),

    # Spice CRUD
    path('spices/', views.add_spice, name='add_spice'),
    path('spices/edit/<int:pk>/', views.edit_spice, name='edit_spice'),
    path('spices/delete/<int:pk>/', views.delete_spice, name='delete_spice'),

    # Pairing CRUD
    path('pairings/', views.paring, name='paring'),
    path('pairings/edit/<int:pk>/', views.edit_pairing, name='edit_pairing'),
    path('pairings/delete/<int:pk>/', views.delete_pairing, name='delete_pairing'),

    # Product CRUD
    path('products/', views.featured_products, name='featured_products'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),

    # Testimonial CRUD
    path('testimonials/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/edit/<int:pk>/', views.edit_testimonial, name='edit_testimonial'),
    path('testimonials/delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),

    # Dashboard for contact messages
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('about/', views.about, name='about'),
    path("stories/", views.story_list, name="story_list"),
    path("stories/add/", views.story_add, name="story_add"),
    path("stories/<int:pk>/edit/", views.story_edit, name="story_edit"),
    path("stories/<int:pk>/delete/", views.story_delete, name="story_delete"),
    path('offline_base/', views.base, name='base'),
     path('offline_index/', views.offline_index, name='offline_index'),
     path('visitor_form/', views.visitor_form, name='visitor_form'),
    path('offline_dashboard_faqs/', views.offline_dashboard_faqs, name='offline_dashboard_faqs'),
    path("faq/edit/<int:pk>/", views.faq_edit, name="edit_faq"),
    path("faq/delete/<int:pk>/", views.faq_delete, name="delete_faq"),
    path('share_event', views.share_event, name='share_event'),
    path('upload/', views.upload_image, name='upload_image'),
    path('blog/', views.Blog, name='blog'),
     # Dashboard
    path('', views.SecurityDashboardView.as_view(), name='dashboard'),
    
    # Statistics API endpoints
    path('api/statistics/', views.GetStatisticsView.as_view(), name='api_statistics'),
    path('api/hourly-data/', views.HourlyDataView.as_view(), name='api_hourly_data'),
    path('api/peak-hours/', views.PeakHoursView.as_view(), name='api_peak_hours'),
    path('api/department-data/', views.DepartmentDataView.as_view(), name='api_department_data'),
    
    # Real-time updates
    path('api/realtime-updates/', views.RealTimeUpdatesView.as_view(), name='api_realtime_updates'),
    
    # Other URLs...
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
