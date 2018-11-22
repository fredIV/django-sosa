from django.urls import path

from .views import *

urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('threejs/', ThreePageView.as_view(), name='threejs'),
    path('boards/', BoardListPageView.as_view(), name='boards'),
    path('stimsets/', StimSetListPageView.as_view(), name='stimsets'),
    path('boards/create/', BoardPageView.as_view(), name='create_board'),
    path('stimsets/create', StimSetPageView.as_view(), name='create_stimulus'),
    path('view_results', ViewResultsPageView.as_view(), name='view_results'),
]
