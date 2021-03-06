from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

Author = settings.AUTH_USER_MODEL


class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    draft = models.BooleanField(default=False)
    pub_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = RichTextUploadingField()
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='article_image', null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(BlogEntry, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
