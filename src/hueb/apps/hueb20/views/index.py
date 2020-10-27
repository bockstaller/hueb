from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "hueb20/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
