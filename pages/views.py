from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from urllib import request
from django.shortcuts import render
from .forms import BoardForm, StimForm
from .models import *


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class LoginPageView(TemplateView):
    template_name = "account/login.html"


class BoardListPageView(TemplateView):
    template_name = "pages/board_list.html"


class BoardPageView(FormView):
    form_class = BoardForm
    template_name = "../templates/pages/create_board.html"
    success_url = reverse_lazy('create_board')

    def form_valid(self, form):
        form.save()
        return super(BoardPageView, self).form_valid(form)


class StimSetListPageView(TemplateView):
    template_name = "pages/stim_sets.html"


class StimSetPageView(FormView):
    form_class = StimForm
    template_name = "../templates/pages/create_stimulus.html"
    success_url = reverse_lazy('create_stimulus')

    def form_valid(self, form):
        form.save()
        return super(StimSetPageView, self).form_valid(form)


class ViewResultsPageView(TemplateView):
    template_name = "pages/view_results.html"


class CreateExperimentPageView(TemplateView):
    template_name = "pages/create_experiment.html"

class ViewExperimentPageView(TemplateView):
    template_name = "pages/view_experiment.html"
