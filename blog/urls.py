from django.urls import path
from .views import HomePageView, PostDetailsView 


urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('post_details/<int:pk>', PostDetailsView.as_view(), name='post_details') 
]
