from django.contrib import admin

from .models import SocialLinks
from .models import TopicCategory

# Register your models here.
admin.site.register(SocialLinks)
admin.site.register(TopicCategory)