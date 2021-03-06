from django.urls import path, re_path, include

from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    # url(r'^experiment/$', 'pages.views.delete_object', name="delete_obj"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('boards/', BoardListPageView.as_view(), name='boards'),
    path('stimsets/', StimSetListPageView.as_view(), name='stimsets'),
    path('boards/create/', BoardCreatePageView.as_view(), name='create_board'),
    path('boards/edit/<int:pk>', BoardEditPageView.as_view(), name='edit_board'),
    path('stimsets/edit/create/<int:stimsetid>', StimCreatePageView.as_view(), name='create_stimulus'),
    path('stimsets/edit/edit_stimulus/<int:pk>', StimEditPageView.as_view(), name='edit_stimulus'),
    path('stimsets/edit/<int:pk>', StimListPageView.as_view(), name='stimuli'),
    path('view_results', ViewResultsPageView.as_view(), name='view_results'),
    path('create_experiment', CreateExperimentPageView.as_view(), name='create_experiment'),
    path(r'experiment/<int:stimsetid>/<int:boardid>', ViewExperimentPageView.as_view(), name='experiment'),
    # path(r'experiment/<int:stimsetid><int:boardid>', ViewExperimentPageView.as_view(), name='experiment'),
]
