from django.db import models
from tabnanny import verbose

# Create your models here.
class Post(models.Model):

    post_title = models.CharField(max_length = 70)
    post_text = models.TextField()
    pub_date = models.DateTimeField("data published")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    text = models.CharField(max_length=70)
    music = models.CharField(max_length=70)

    def __str__(self):
        return self.post_text

