from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('career/', views.career_page, name='career'),
    path('contact/', views.contact, name='contact'),
    path('corporate/', views.corporate, name='corporate'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('exhibition/', views.exhibition, name='exhibition'),
    path('facilities/', views.facilities, name='facilities'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('plan_event/', views.plan_event, name='plan_event'),
    path('privacy/', views.privacy, name='privacy'),
    path('product_launch/', views.product_launch, name='product_launch'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('social_events/', views.social_events, name='social_events'),
    path('terms/', views.terms, name='terms'),
    path('themes/', views.themes, name='themes'),
    path('wedding/', views.wedding, name='wedding'),
]