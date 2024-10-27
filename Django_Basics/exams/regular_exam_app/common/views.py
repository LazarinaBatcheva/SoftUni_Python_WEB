from django.views.generic import TemplateView, ListView
from posts.models import Post
from regular_exam_app.utils import get_author_obj


class IndexPageView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_author_obj()

        return context


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
