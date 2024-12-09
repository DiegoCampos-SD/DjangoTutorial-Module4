from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.publishedDate = timezone.now()
        self.save()
    
    def approved_comments(self):
        return self.comments.filter(approvedComment=True)
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('blogDiego.Post', on_delete=models.CASCADE, related_name='comments', db_column='post')
    author = models.CharField(max_length=200)
    text = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    approvedComment = models.BooleanField(default=False)

    def approve(self):
        self.approvedComment = True
        self.save()

    def __str__(self):
        return self.text