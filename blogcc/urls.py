from . import views
from django.urls import path 


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('blogs/', views.BlogPostList.as_view(), name='blogs')
]