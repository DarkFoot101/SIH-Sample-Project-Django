from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import views once

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:alumni_id>/', views.profile, name='profile_with_id'),  # Single profile URL
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),

    path('resume-matcher/', views.resume_matcher, name='resume_matcher'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('radar-plot/', views.radar_plot, name='radar_plot'),
    path("pdf-analyzer/", views.pdf_analyzer, name="pdf_analyzer")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)