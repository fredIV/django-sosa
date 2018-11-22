from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ThreePageView(TemplateView):
    template_name = "pages/threejs.html"


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
