from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField

User = get_user_model()

# Create your models here.

class Category(models.Model):
    name_category = models.CharField(max_length=200, unique=True)
    slug_category = models.SlugField(allow_unicode=True, max_length=200, unique=True, editable=False, default='')

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.name_category)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_category

class Subcategory(models.Model):
    name_subcategory = models.CharField(max_length=200, unique=True)
    slug_subcategory = models.SlugField(allow_unicode=True, max_length=200, unique=True, editable=False, default='')
    main_category = models.ForeignKey(Category, related_name='relation_subcategory', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug_subcategory = slugify(self.name_subcategory)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_subcategory

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(allow_unicode=True, max_length=200, unique=True, editable=False, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('blog_app:post_detail', kwargs=kwargs)

    def __str__(self):
        return self.title
