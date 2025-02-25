from django.db import models
from user_auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='blog_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog_image")
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
