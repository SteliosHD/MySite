from django.urls import path
from .views import (
    HomeView,
    PortfolioView,
)
from . import views # . is the current directory


urlpatterns = [
    # path('', PostListView.as_view(), name = 'contact-home'),
    path('', HomeView.as_view(extra_context={'title': 'Home'}), name='contact-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    # path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    # path('about/', views.about, name = 'contact-about'),
    # path('resume/', views.resume, name='contact-resume'),
    # path('contact/', views.contact, name='contact-contact'),
    path('portfolio/', PortfolioView.as_view(extra_context={'title': 'Portfolio'}), name='contact-portfolio'),
]
