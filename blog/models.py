from django.db import models
from django.core.urlresolvers import reverse
import datetime

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"id": self.id})
        ##return "/blog/%s" %(self.id)