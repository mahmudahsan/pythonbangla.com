from django.db import models

class SocialLinks(models.Model):
    name = models.CharField(max_length=30)
    url = models.TextField()

    def __str__(self):
        return self.name

class TopicCategory(models.Model):
    title_english = models.CharField(max_length=100,)
    title_other = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    image_name = models.CharField(max_length=50)
    topic_type = (
        ('YT', 'Youtube'),
        ('UR', "URL"),
    )

    def __str__(self):
        return self.title_english + " | " + self.title_other
