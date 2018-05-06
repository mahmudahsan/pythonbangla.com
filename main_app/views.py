from django.views.generic import TemplateView
from .models import SocialLink, TopicCategory

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
         context = super(HomeView, self).get_context_data(**kwargs)
         context['social'] = SocialLink.objects.all().order_by('pk')
         context['topic_category'] = TopicCategory.objects.all().order_by('pk')
         return context