from django.views.generic import TemplateView
from django.shortcuts import render
from .form import BoardForm
from .models import *


def add_board(request):
    success = False

    if request.method == "POST":
        board_form = BoardForm(request.POST)

        if board_form.is_valid():
            success = True

            boardname = board_form.cleaned_data['boardname']

            new_board = Boards(boardname=boardname)
            new_board.save()

            new_board_form = BoardForm()
            bfx2 = {'success':success, 'board_form': new_board_form}
            return render('templates/pages/create_board.html', bfx2)
    else:
        board_form = BoardForm()
    bf = {'board_form': board_form}
    return render('templates/pages/create_board.html', bf)


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class LoginPageView(TemplateView):
    template_name = "account/login.html"


class BoardListPageView(TemplateView):
    template_name = "pages/board_list.html"


class BoardPageView(TemplateView):
    template_name = "pages/create_board.html"


class StimSetListPageView(TemplateView):
    template_name = "pages/stim_sets.html"


class StimSetPageView(TemplateView):
    template_name = "pages/create_stimulus.html"


class ViewResultsPageView(TemplateView):
    template_name = "pages/view_results.html"


class CreateExperimentPageView(TemplateView):
    template_name = "pages/create_experiment.html"
