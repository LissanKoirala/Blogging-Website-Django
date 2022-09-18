from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog-home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    #content = RichTextField(blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    post_image = models.ImageField(null=True, blank=True, upload_to="user_posts_images/")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author) 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
 
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    your_name = models.CharField(max_length=30)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s | %s" % (self.post.title, self.name)

