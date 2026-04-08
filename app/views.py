from django.shortcuts import render, redirect, get_object_or_404
from .models import Story, faq
from django.contrib import messages
from .models import (
    SpiceCollection, Flavor, Receipe, Spice,
    Pairing, Category, Product, Testimonial, ContactMessage,Blog
)
from .forms import (
    SpiceCollectionForm, FlavorForm, ReceipeForm,
    SpiceForm, PairingForm, ProductForm,
    TestimonialForm, ContactForm,
)

# ------------------ Frontend (Index Page) ------------------
def index(request):
    spices = SpiceCollection.objects.all()
    flavors = Flavor.objects.all()
    recipes = Receipe.objects.all()
    spices_card = Spice.objects.all()
    products = Product.objects.all()
    pairings = Pairing.objects.all()
    testimonials = Testimonial.objects.all().order_by('-created_at')
    
    

    return render(request, 'index.html', {
        "Spicesxx": spices_card,
        "flavors": flavors,
        "recipes": recipes,
        "collections": spices,
        "pairings": pairings,
        "products": products,
        "testimonials": testimonials,
        "faqs": faq.objects.all().order_by('sequence'),
    })

# ------------------ Admin: SpiceCollection ------------------

def add_spice_collection(request):
    if request.method == 'POST':
        form = SpiceCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_spice_collection')
    else:
        form = SpiceCollectionForm()

    collections = SpiceCollection.objects.all()
    return render(request, 'add.html', {"form": form, "collections": collections})

def edit_spice_collection(request, pk):
    collection = get_object_or_404(SpiceCollection, pk=pk)
    if request.method == "POST":
        form = SpiceCollectionForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('add_spice_collection')
    else:
        form = SpiceCollectionForm(instance=collection)
    return render(request, 'add.html', {'form': form})

def delete_spice_collection(request, pk):
    collection = get_object_or_404(SpiceCollection, pk=pk)
    collection.delete()
    return redirect('add_spice_collection')

# ------------------ Admin: Flavor ------------------
def shop_by_flavour(request):
    if request.method == 'POST':
        form = FlavorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_by_flavour')
    else:
        form = FlavorForm()
    flavors = Flavor.objects.all()
    return render(request, 'shop_by_flavour.html', {"form": form, "flavors": flavors})

def edit_flavor(request, pk):
    flavor = get_object_or_404(Flavor, pk=pk)
    if request.method == "POST":
        form = FlavorForm(request.POST, request.FILES, instance=flavor)
        if form.is_valid():
            form.save()
            return redirect('shop_by_flavour')
    else:
        form = FlavorForm(instance=flavor)
    return render(request, 'shop_by_flavour.html', {'form': form})

def delete_flavor(request, pk):
    flavor = get_object_or_404(Flavor, pk=pk)
    flavor.delete()
    return redirect('shop_by_flavour')

# ------------------ Admin: Recipe ------------------
def receipe(request):
    if request.method == 'POST':
        form = ReceipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('receipe')
    else:
        form = ReceipeForm()
    recipes = Receipe.objects.all()
    return render(request, 'receipe.html', {"form": form, "recipes": recipes})

def edit_receipe(request, pk):
    recipe = get_object_or_404(Receipe, pk=pk)
    if request.method == "POST":
        form = ReceipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('receipe')
    else:
        form = ReceipeForm(instance=recipe)
    return render(request, 'receipe.html', {'form': form})

def delete_receipe(request, pk):
    recipe = get_object_or_404(Receipe, pk=pk)
    recipe.delete()
    return redirect('receipe')

# ------------------ Admin: Spice ------------------
def add_spice(request):
    if request.method == "POST":
        form = SpiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("add_spice")
    else:
        form = SpiceForm()
    spices = Spice.objects.all()
    return render(request, "Spicex.html", {"form": form, "Spicesxx": spices})

def edit_spice(request, pk):
    spice = get_object_or_404(Spice, pk=pk)
    if request.method == "POST":
        form = SpiceForm(request.POST, request.FILES, instance=spice)
        if form.is_valid():
            form.save()
            return redirect('add_spice')
    else:
        form = SpiceForm(instance=spice)
    return render(request, "Spicex.html", {'form': form})

def delete_spice(request, pk):
    spice = get_object_or_404(Spice, pk=pk)
    spice.delete()
    return redirect('add_spice')

# ------------------ Admin: Pairing ------------------
def paring(request):
    if request.method == "POST":
        name = request.POST.get("name")
        aroma = request.POST.get("aroma")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        categories = request.POST.get("categories") 
        vegan = request.POST.get("vegan") # text field

        pairing = Pairing.objects.create(
            name=name,
            aroma=aroma,
            price=price,
            description=description,
            image=image,
            categories=categories,
            vegan=vegan
        )
        return redirect("paring")

    pairings = Pairing.objects.all()
    return render(request, "add_pairing.html", {"pairings": pairings})

def edit_pairing(request, pk):
    pairing = get_object_or_404(Pairing, pk=pk)
    if request.method == "POST":
        form = PairingForm(request.POST, request.FILES, instance=pairing)
        if form.is_valid():
            form.save()
            return redirect('paring')
    else:
        form = PairingForm(instance=pairing)
    categories = Category.objects.all()
    return render(request, 'add_pairing.html', {'form': form, 'categories': categories})

def delete_pairing(request, pk):
    pairing = get_object_or_404(Pairing, pk=pk)
    pairing.delete()
    return redirect('paring')

# ------------------ Admin: Product ------------------
def featured_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('featured_products')
    else:
        form = ProductForm()
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'featured_products.html', {'form': form, 'products': products})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('featured_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'featured_products.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('featured_products')

# ------------------ Admin: Testimonial ------------------
def add_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_testimonial')
    else:
        form = TestimonialForm()
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'testimonial_form.html', {'form': form, 'testimonials': testimonials})

def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('add_testimonial')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'testimonial_form.html', {'form': form})

def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    return redirect('add_testimonial')

# ------------------ Contact ------------------
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your form has been submitted!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def dashboard_view(request):
    submissions = ContactMessage.objects.all().order_by('-submitted_at')
    return render(request, 'dashboard.html', {'submissions': submissions})










def about(request):
    content={}
    content['testimonials'] = Testimonial.objects.all().order_by('-created_at')
    content['stories']=Story.objects.all()
    content['faqs'] = faq.objects.all().order_by('sequence')
    

    return render(request, 'about.html',content)

def base(request):
 return render(request, 'offline_base.html')

def offline_index(request):
    return render(request, 'offline_index.html')

def visitor_form(request):
    return render(request, 'visitor_form.html')




    
    



from django.shortcuts import render, get_object_or_404, redirect
from .models import Story
from .forms import StoryForm

# List all stories
from django.shortcuts import render, redirect, get_object_or_404
from .models import Story
from .forms import StoryForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Story
from .forms import StoryForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Story,faq
from .forms import StoryForm

# List all stories
def story_list(request):
    stories = Story.objects.all()
    return render(request, "story_list.html", {"stories": stories})


# Add new story
def story_add(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("story_list")
    else:
        form = StoryForm()
    return render(request, "story_form.html", {"form": form, "action": "Add"})


# Edit existing story
def story_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            return redirect("story_list")
    else:
        form = StoryForm(instance=story)
    return render(request, "story_form.html", {"form": form, "action": "Edit"})


# Delete story
def story_delete(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        story.delete()
        return redirect("story_list")
    return render(request, "story_confirm_delete.html", {"story": story})



from django.shortcuts import render, redirect
from .models import faq

def offline_dashboard_faqs(request):
    content = {}
    faqs = faq.objects.all()
    content['faqs'] = faqs

    if request.method == 'POST':
        data = request.POST
        print("POST Data:", data)
        
        faq.objects.create(
            question=data['question'],
            answer=data['answer'],
            sequence=int(data['sequence']),
        )
        return redirect('offline_dashboard_faqs')  # redirect after POST to avoid resubmission

    return render(request, 'offline_dashboard_faqs.html', content)




def faq_edit(request, pk):
    f = get_object_or_404(faq, pk=pk)
    if request.method == "POST":
        f.question = request.POST.get("question")
        f.answer = request.POST.get("answer")
        f.sequence = request.POST.get("sequence")
        f.save()
        return redirect("offline_dashboard_faqs")  # back to list
    return redirect("offline_dashboard_faqs")

def faq_delete(request, pk):
    f = get_object_or_404(faq, pk=pk)
    if request.method == "POST":
        f.delete()
        return redirect("offline_dashboard_faqs")  # back to list
    return redirect("offline_dashboard_faqs")
from django.db import models



from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from datetime import datetime

def share_event(request):
    return render(request, 'share.html')


@csrf_exempt  # 
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + image.name
        filepath = os.path.join(settings.MEDIA_ROOT, filename)

        with open(filepath, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        image_url = request.build_absolute_uri(settings.MEDIA_URL + filename)
        return JsonResponse({"image_url": image_url})

    return JsonResponse({"error": "No image uploaded"}, status=400)



def blogs(request):
    blog = blog.object.all()
    return render(request,'index.html',{'blog':blog})




from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
import json
from datetime import datetime, timedelta

from .models import Visitor, Host, SecurityGuard, VisitorLog, Blacklist
from .forms import VisitorCheckinForm, QuickCheckinForm, VisitorCheckoutForm, SearchForm, SecurityGuardLoginForm

class SecurityDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'visitors/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get current guard
        try:
            guard = SecurityGuard.objects.get(user=self.request.user)
            context['guard'] = guard
        except SecurityGuard.DoesNotExist:
            guard = None
        
        # Get today's statistics
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        
        # Today's visitors
        today_visitors = Visitor.objects.filter(check_in_time__range=(today_start, today_end))
        
        context.update({
            'total_today': today_visitors.count(),
            'checked_in': today_visitors.filter(status='checked_in').count(),
            'checked_out': today_visitors.filter(status='checked_out').count(),
            'overdue': today_visitors.filter(status='overdue').count(),
            
            # Recent visitors
            'recent_visitors': Visitor.objects.all().order_by('-check_in_time')[:10],
            
            # Visitors by type
            'visitor_types': today_visitors.values('visitor_type').annotate(count=Count('id')),
            
            # Hosts with most visitors today
            'top_hosts': today_visitors.values('host__name').annotate(
                count=Count('id')
            ).order_by('-count')[:5],
        })
        
        return context

class VisitorCheckinView(LoginRequiredMixin, View):
    template_name = 'checkin.html'
    
    def get(self, request):
        context = {
            'form': VisitorCheckinForm(),
            'quick_form': QuickCheckinForm(),
            'hosts': Host.objects.filter(is_active=True),
            'recent_visitors': Visitor.objects.filter(
                check_in_time__date=timezone.now().date()
            ).order_by('-check_in_time')[:5]
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = VisitorCheckinForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                # Get current guard
                guard = SecurityGuard.objects.get(user=request.user)
                
                # Create visitor instance
                visitor = form.save(commit=False)
                visitor.checked_in_by = guard
                visitor.status = 'checked_in'
                
                # Convert items_brought from list to JSON
                if 'items_brought' in form.cleaned_data:
                    visitor.items_brought = form.cleaned_data['items_brought']
                
                visitor.save()
                
                # Create log entry
                VisitorLog.objects.create(
                    visitor=visitor,
                    action='check_in',
                    performed_by=guard,
                    notes=f"Checked in by {guard.user.get_full_name()} at {guard.gate}",
                    ip_address=request.META.get('REMOTE_ADDR')
                )
                
                # Notify host (simulate)
                self._notify_host(visitor)
                
                messages.success(
                    request,
                    f'Visitor {visitor.get_full_name()} checked in successfully! '
                    f'Badge: {visitor.badge_number}'
                )
                
                # Return success response for AJAX
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': True,
                        'visitor_id': visitor.visitor_id,
                        'badge_number': visitor.badge_number,
                        'name': visitor.get_full_name(),
                        'message': 'Visitor checked in successfully'
                    })
                
                return redirect('visitor_detail', pk=visitor.pk)
                
            except Exception as e:
                messages.error(request, f'Error checking in visitor: {str(e)}')
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': str(e)})
        else:
            errors = form.errors.as_json()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': errors})
        
        context = {
            'form': form,
            'quick_form': QuickCheckinForm(),
            'hosts': Host.objects.filter(is_active=True),
        }
        return render(request, self.template_name, context)
    
    def _notify_host(self, visitor):
        """Simulate host notification"""
        # In a real application, this would send email/SMS
        pass

class QuickCheckinView(LoginRequiredMixin, View):
    def post(self, request):
        form = QuickCheckinForm(request.POST)
        
        if form.is_valid():
            qr_code = form.cleaned_data.get('qr_code')
            visitor_id = form.cleaned_data.get('visitor_id')
            
            # Logic for quick check-in
            # This would typically retrieve pre-registered visitor data
            return JsonResponse({
                'success': True,
                'message': 'Quick check-in processed'
            })
        
        return JsonResponse({
            'success': False,
            'errors': form.errors.as_json()
        })

class VisitorCheckoutView(LoginRequiredMixin, View):
    template_name = 'visitors/checkout.html'
    
    def get(self, request):
        context = {
            'form': VisitorCheckoutForm(),
            'checked_in_visitors': Visitor.objects.filter(status='checked_in')
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = VisitorCheckoutForm(request.POST)
        
        if form.is_valid():
            visitor_id = form.cleaned_data['visitor_id']
            check_out_time = form.cleaned_data['check_out_time']
            notes = form.cleaned_data['notes']
            
            try:
                # Find visitor by ID or badge number
                visitor = Visitor.objects.get(
                    Q(visitor_id=visitor_id) | Q(badge_number=visitor_id),
                    status='checked_in'
                )
                
                # Get current guard
                guard = SecurityGuard.objects.get(user=request.user)
                
                # Update visitor
                visitor.check_out_time = check_out_time
                visitor.checked_out_by = guard
                visitor.status = 'checked_out'
                visitor.save()
                
                # Create log entry
                VisitorLog.objects.create(
                    visitor=visitor,
                    action='check_out',
                    performed_by=guard,
                    notes=notes or f"Checked out by {guard.user.get_full_name()}",
                    ip_address=request.META.get('REMOTE_ADDR')
                )
                
                messages.success(
                    request,
                    f'Visitor {visitor.get_full_name()} checked out successfully!'
                )
                
                return redirect('dashboard')
                
            except Visitor.DoesNotExist:
                messages.error(request, 'Visitor not found or already checked out')
            except Exception as e:
                messages.error(request, f'Error during checkout: {str(e)}')
        
        context = {
            'form': form,
            'checked_in_visitors': Visitor.objects.filter(status='checked_in')
        }
        return render(request, self.template_name, context)

class VisitorListView(LoginRequiredMixin, ListView):
    model = Visitor
    template_name = 'visitors/visitor_list.html'
    paginate_by = 20
    context_object_name = 'visitors'
    
    def get_queryset(self):
        queryset = Visitor.objects.all().order_by('-check_in_time')
        
        # Filter by status
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by date
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        
        if date_from:
            queryset = queryset.filter(check_in_time__date__gte=date_from)
        if date_to:
            queryset = queryset.filter(check_in_time__date__lte=date_to)
        
        # Search
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(company__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(visitor_id__icontains=search_query) |
                Q(badge_number__icontains=search_query) |
                Q(host__name__icontains=search_query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)
        context['status_choices'] = Visitor.STATUS_CHOICES
        return context

class VisitorDetailView(LoginRequiredMixin, DetailView):
    model = Visitor
    template_name = 'visitors/visitor_detail.html'
    context_object_name = 'visitor'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logs'] = VisitorLog.objects.filter(visitor=self.object).order_by('-timestamp')
        return context

class CheckBlacklistView(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        id_number = data.get('id_number')
        id_type = data.get('id_type')
        
        if id_number and id_type:
            blacklisted = Blacklist.objects.filter(
                id_number=id_number,
                id_type=id_type,
                is_active=True
            ).exists()
            
            return JsonResponse({
                'blacklisted': blacklisted,
                'message': 'Blacklisted' if blacklisted else 'Not blacklisted'
            })
        
        return JsonResponse({'error': 'Missing data'}, status=400)

class GetStatisticsView(LoginRequiredMixin, View):
    def get(self, request):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        
        today_visitors = Visitor.objects.filter(check_in_time__range=(today_start, today_end))
        
        # Daily stats for chart
        last_7_days = []
        for i in range(7):
            date = timezone.now().date() - timedelta(days=i)
            day_start = timezone.make_aware(datetime.combine(date, datetime.min.time()))
            day_end = day_start + timedelta(days=1)
            
            count = Visitor.objects.filter(check_in_time__range=(day_start, day_end)).count()
            last_7_days.append({
                'date': date.strftime('%Y-%m-%d'),
                'count': count
            })
        
        last_7_days.reverse()
        
        return JsonResponse({
            'today': {
                'total': today_visitors.count(),
                'checked_in': today_visitors.filter(status='checked_in').count(),
                'checked_out': today_visitors.filter(status='checked_out').count(),
                'overdue': today_visitors.filter(status='overdue').count(),
            },
            'last_7_days': last_7_days,
            'visitor_types': list(today_visitors.values('visitor_type').annotate(
                count=Count('id')
            )),
        })

class PrintBadgeView(LoginRequiredMixin, View):
    def get(self, request, visitor_id):
        visitor = get_object_or_404(Visitor, visitor_id=visitor_id)
        
        # Create log entry
        guard = SecurityGuard.objects.get(user=request.user)
        VisitorLog.objects.create(
            visitor=visitor,
            action='badge_printed',
            performed_by=guard,
            notes=f'Badge printed for {visitor.get_full_name()}',
            ip_address=request.META.get('REMOTE_ADDR')
        )
        
        # Return badge HTML for printing
        context = {'visitor': visitor}
        return render(request, 'visitors/badge_print.html', context)

# API Views for mobile/tablet access
class APIVisitorCheckin(View):
    def post(self, request):
        """API endpoint for mobile check-in"""
        try:
            data = json.loads(request.body)
            
            # Validate guard token/credentials
            guard_id = data.get('guard_id')
            guard_token = data.get('guard_token')
            
            # In real app, validate guard credentials
            
            # Create visitor
            visitor_data = data.get('visitor')
            form = VisitorCheckinForm(visitor_data)
            
            if form.is_valid():
                visitor = form.save()
                
                return JsonResponse({
                    'success': True,
                    'visitor_id': visitor.visitor_id,
                    'badge_number': visitor.badge_number,
                    'message': 'Visitor checked in successfully'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

@login_required
def search_visitors(request):
    """AJAX search endpoint"""
    query = request.GET.get('q', '')
    
    if query:
        visitors = Visitor.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(company__icontains=query) |
            Q(phone__icontains=query) |
            Q(visitor_id__icontains=query) |
            Q(badge_number__icontains=query)
        )[:10]
        
        results = [{
            'id': v.id,
            'visitor_id': v.visitor_id,
            'name': v.get_full_name(),
            'company': v.company,
            'phone': v.phone,
            'badge_number': v.badge_number,
            'status': v.status,
            'check_in_time': v.check_in_time.strftime('%Y-%m-%d %H:%M'),
            'host': v.host.name if v.host else ''
        } for v in visitors]
        
        return JsonResponse({'results': results})
    
    return JsonResponse({'results': []})

# Custom login view for security guards
def security_guard_login(request):
    if request.method == 'POST':
        form = SecurityGuardLoginForm(request.POST)
        if form.is_valid():
            guard_id = form.cleaned_data['guard_id']
            password = form.cleaned_data['password']
            gate = form.cleaned_data['gate']
            
            # Custom authentication logic for security guards
            # In a real app, integrate with Django's auth system
            
            # For now, redirect to dashboard
            return redirect('dashboard')
    else:
        form = SecurityGuardLoginForm()
    
    return render(request, 'visitors/guard_login.html', {'form': form})



# Create additional API views for real-time data
class HourlyDataView(LoginRequiredMixin, View):
    def get(self, request):
        date_str = request.GET.get('date', timezone.now().date().isoformat())
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        hourly_data = []
        for hour in range(24):
            hour_start = timezone.make_aware(datetime.combine(date, datetime.min.time())) + timedelta(hours=hour)
            hour_end = hour_start + timedelta(hours=1)
            
            count = Visitor.objects.filter(
                check_in_time__range=(hour_start, hour_end)
            ).count()
            
            hourly_data.append({
                'hour': f"{hour:02d}:00",
                'count': count
            })
        
        return JsonResponse({'hourly_data': hourly_data})

class PeakHoursView(LoginRequiredMixin, View):
    def get(self, request):
        days = int(request.GET.get('days', 7))
        start_date = timezone.now() - timedelta(days=days)
        
        peak_data = []
        for hour in range(24):
            count = Visitor.objects.filter(
                check_in_time__gte=start_date,
                check_in_time__hour=hour
            ).count()
            
            peak_data.append({
                'hour': f"{hour:02d}:00",
                'count': count
            })
        
        return JsonResponse({'peak_data': peak_data})

class DepartmentDataView(LoginRequiredMixin, View):
    def get(self, request):
        days = int(request.GET.get('days', 1))
        start_date = timezone.now() - timedelta(days=days)
        
        dept_data = list(Visitor.objects.filter(
            check_in_time__gte=start_date
        ).values(
            'host__department'
        ).annotate(
            count=Count('id')
        ).order_by('-count'))
        
        return JsonResponse({'department_data': dept_data})

class RealTimeUpdatesView(LoginRequiredMixin, View):
    def get(self, request):
        """SSE endpoint for real-time updates"""
        # This would implement Server-Sent Events for real-time updates
        response = HttpResponse(content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        response['Connection'] = 'keep-alive'
        
        def event_stream():
            while True:
                # Get latest data
                data = {
                    'current_visitors': Visitor.objects.filter(status='checked_in').count(),
                    'today_total': Visitor.objects.filter(
                        check_in_time__date=timezone.now().date()
                    ).count(),
                    'recent_checkins': list(Visitor.objects.filter(
                        check_in_time__gte=timezone.now() - timedelta(minutes=5)
                    ).values('first_name', 'last_name', 'company', 'badge_number')[:5])
                }
                
                yield f"data: {json.dumps(data)}\n\n"
                time.sleep(30)  # Update every 30 seconds
        
        response.streaming_content = event_stream()
        return response
    


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("visitor_dashboard")  # 👈 dashboard
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")



    