from django.shortcuts import render
from admins.models import Portfolio, Gallery, TeamMember, JobOpening,Facility,Blog,FAQ,Term,PrivacyPolicy
from django.shortcuts import render, redirect
from admins.models import Portfolio, Gallery, FeaturedEvent, Testimonial
from main.models import EventBooking, ContactEnquiry
# Create your views here.
def home(request):
    featured_events = FeaturedEvent.objects.filter(is_active=True).order_by('-created_at')
    testimonials = Testimonial.objects.all().order_by('-created_at')

    return render(request, "main/index.html", {
        "featured_events": featured_events,
        "testimonials": testimonials,
    })
def about(request):
    team_members = TeamMember.objects.filter(is_active=True).order_by('-created_at')

    return render(request, "main/about.html", {
        'team_members': team_members
    })

def blog(request):
    posts = Blog.objects.all().order_by('-date')
    return render(request, "main/blog.html", {'posts': posts})


def career_page(request):
    jobs = JobOpening.objects.all().order_by('-created_at')
    return render(request, 'main/carrer.html', {'jobs': jobs})
    
    


def contact(request):
    if request.method == 'POST':
        ContactEnquiry.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            event_type=request.POST.get('event_type'),
            message=request.POST.get('message')
        )
        # Change 'contact' to whatever your page URL name is
        return redirect('contact') 

    return render(request, 'main/contact.html')

def corporate(request):
    return render(request, "main/corporate.html")

def entertainment(request):
    return render(request, "main/entertainment.html")

def exhibition(request):
    return render(request, "main/exhibition.html")

def facilities(request):
    facilities_list = Facility.objects.all().order_by('-created_at')
    return render(request, "main/facilities.html", {'facilities': facilities_list})

def faq(request):
    faqs = FAQ.objects.all().order_by('created_at') # Or '-created_at' for newest first
    return render(request, "main/FAQ.html", {'faqs': faqs})

def gallery(request):
    images = Gallery.objects.all().order_by('-created_at')
    return render(request, "main/gallery.html", {'images': images})

def plan_event(request):
    if request.method == "POST":
        try:
            EventBooking.objects.create(
                event_type=request.POST.get('event_type'),
                event_date=request.POST.get('event_date'),
                event_city=request.POST.get('event_city'),
                expected_guests=request.POST.get('expected_guests'),
                event_budget=request.POST.get('event_budget'),
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                mobile_number=request.POST.get('mobile_number'),
                additional_info=request.POST.get('additional_info')
            )
            return redirect('plan_event') 
            
        except Exception as e:
            return redirect('plan_event')

    return render(request, 'main/plan-event.html')

def privacy(request):
    policies = PrivacyPolicy.objects.all().order_by('order')
    return render(request, "main/privacy.html", {'policies': policies})

def product_launch(request):
    return render(request, "main/product-launch.html")

def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, "main/portfolio.html", {'portfolios': portfolios})

def services(request):
    return render(request, "main/services.html")

def social_events(request):
    return render(request, "main/social-events.html")

def terms(request):
    terms_list = Term.objects.all().order_by('-order')
    return render(request, "main/terms.html", {'terms_list': terms_list})

def themes(request):
    return render(request, "main/themes.html")

def wedding(request):
    return render(request, "main/wedding.html")

