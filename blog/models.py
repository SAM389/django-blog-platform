from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('all', 'All'),
        ('science', 'Science'),
        ('history', 'History'),
        ('entertainment', 'Entertainment'),
        ('sports', 'Sports'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='all')
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    bookmarks = models.ManyToManyField(User, related_name='blog_bookmarks', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()
    
    def total_bookmarks(self):
        return self.bookmarks.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})


