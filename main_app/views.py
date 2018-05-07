from django.views.generic import TemplateView
from .models import SocialLink
from .models import TopicCategory
from .models import TopicContent

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['social'] = SocialLink.objects.all().order_by('pk')
        context['topic_category'] = TopicCategory.objects.all().order_by('pk')

        for topic in context['topic_category']:
            topic.contents = TopicContent.objects.filter(topic_category=topic.id).order_by('pk')

        for topic in context['topic_category']:
            print(topic.contents)

        # print(context['topic_category'])
        return context