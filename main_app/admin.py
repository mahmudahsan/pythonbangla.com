from django.contrib import admin

from .models import SocialLink
from .models import TopicCategory
from .models import TopicContent

# Register your models here.
admin.site.register(SocialLink)
admin.site.register(TopicCategory)
admin.site.register(TopicContent)