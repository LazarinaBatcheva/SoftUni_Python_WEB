from django.views.generic import TemplateView
from world_of_speed_app.utils import get_profile_obj


class IndexPageView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile_obj()

        return context
