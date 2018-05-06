from django.views.generic import TemplateView
from .models import SocialLinks, TopicCategory

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
         context = super(HomeView, self).get_context_data(**kwargs)
         context['social'] = SocialLinks.objects.all()
         context['topic_category'] = TopicCategory.objects.all()
         return context