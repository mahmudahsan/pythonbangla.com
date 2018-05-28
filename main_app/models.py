from django.db import models

class SocialLink(models.Model):
    name = models.CharField(max_length=30)
    url = models.TextField()

    def __str__(self):
        return self.name

class TopicCategory(models.Model):
    title_english = models.CharField(max_length=100)
    title_other = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    image_name = models.CharField(max_length=50)

    YOUTUBE = 'YT'
    URL     = 'UR'
    topic_choice = (
        ('YT', 'Youtube'), 
        ('UR', "URL"),
    )

    topic_type = models.CharField(
        max_length=2,
        choices=topic_choice,
        default=YOUTUBE,
    )

    order = models.FloatField(default=0)

    def __str__(self):
        return self.title_english + " | " + self.title_other

class TopicContent(models.Model):
    topic_category = models.ForeignKey(
        'TopicCategory',
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True, null=True)
    video_id = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=200, default=None, blank=True, null=True)
    tag = models.CharField(max_length=40, default=None, blank=True, null=True)
    order = models.FloatField(default=0)

    def __str__(self):
        return self.title

class SiteOption(models.Model):
    header = models.TextField(default='', blank=True, null=True)
    title  = models.CharField(max_length=200, default=None, blank=True, null=True)
    meta_author = models.CharField(max_length=100, default=None, blank=True, null=True)
    meta_description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return "Customize frontend from admin panel"