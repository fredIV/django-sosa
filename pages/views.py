from django.views.generic import TemplateView, FormView, ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from urllib import request
from django.shortcuts import render
from .forms import *
from .models import *


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class LoginPageView(TemplateView):
    template_name = "account/login.html"


class BoardListPageView(ListView):
    template_name = "pages/board_list.html"
    model = Boards
    queryset = Boards.objects.all()
    context_object_name = "boards"


class BoardCreatePageView(FormView):
    form_class = BoardForm
    template_name = "../templates/pages/create_board.html"
    success_url = reverse_lazy('boards')

    def form_valid(self, form):
        form.save()
        return super(BoardCreatePageView, self).form_valid(form)


class BoardEditPageView(UpdateView):
    model = Boards
    context_object_name = "boards"
    form_class = BoardEditForm
    template_name = "../templates/pages/edit_board.html"
    success_url = reverse_lazy('boards')


class StimSetListPageView(CreateView, ListView):
    model = StimSets
    template_name = "../templates/pages/stim_sets.html"
    queryset = StimSets.objects.all()
    context_object_name = "stimsets"
    form_class = StimSetForm
    success_url = reverse_lazy('stimsets')


class StimListPageView(ListView):
    model = Stims
    template_name = "pages/stimuli.html"
    queryset = Stims.objects.all()
    context_object_name = "stimuli"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StimListPageView, self).get_context_data(**kwargs)
        context['stimsets'] = StimSets.objects.all()
        return context


class StimCreatePageView(FormView):
    form_class = StimForm
    template_name = "../templates/pages/create_stimulus.html"
    success_url = reverse_lazy('stimsets')

    def form_valid(self, form):
        form.save()
        return super(StimCreatePageView, self).form_valid(form)


class StimEditPageView(UpdateView):
    model = Stims
    context_object_name = "stimuli"
    form_class = StimEditForm
    template_name = "../templates/pages/edit_stimulus.html"
    success_url = reverse_lazy('stimsets')


class ViewResultsPageView(TemplateView):
    template_name = "pages/view_results.html"


class CreateExperimentPageView(ListView):
    template_name = "pages/create_experiment.html"
    model = Boards
    queryset = Boards.objects.all()
    context_object_name = "boards"

    def get_context_data(self, **kwargs):
        context = super(CreateExperimentPageView, self).get_context_data(**kwargs)
        context['stimsets'] = StimSets.objects.all()
        # And so on for more models
        return context



class ViewExperimentPageView(TemplateView):
    template_name = "pages/view_experiment.html"
