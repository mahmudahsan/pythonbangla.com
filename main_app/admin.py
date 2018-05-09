from django.contrib import admin

from .models import SocialLink
from .models import TopicCategory
from .models import TopicContent
from .models import SiteOption

# Register your models here.
admin.site.register(SocialLink)
admin.site.register(TopicCategory)
admin.site.register(TopicContent)
admin.site.register(SiteOption)