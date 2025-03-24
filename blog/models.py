from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    meta_description = models.CharField(max_length=200, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    content_step_1 = models.TextField(default='')
    content_step_2 = models.TextField(default='')
    content_step_3 = models.TextField(default='')
    content_step_4= models.TextField(default='')
    content_step_5= models.TextField(default='')
    image = models.ImageField(upload_to='blog_images/', blank=True)
    image_step_1 = models.ImageField(upload_to='blog_images/', blank=True)
    image_step_2 = models.ImageField(upload_to='blog_images/', blank=True)
    image_step_3 = models.ImageField(upload_to='blog_images/', blank=True)
    image_step_4 = models.ImageField(upload_to='blog_images/', blank=True)
    image_step_5 = models.ImageField(upload_to='blog_images/', blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
