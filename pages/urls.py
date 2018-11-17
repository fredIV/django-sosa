from django.urls import path

from .views import HomePageView, AboutPageView, ThreePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('threejs/', ThreePageView.as_view(), name='threejs'),

]
