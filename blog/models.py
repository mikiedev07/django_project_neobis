from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse
import datetime


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='post_pics/', null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def was_published_recently(self):
		return self.date_posted >= (timezone.now() - datetime.timedelta(days=7))


class Announcement(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='announcement_pics/', null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def was_published_recently(self):
		return self.date_posted >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_post')
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	content = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)
	status = models.BooleanField(verbose_name='post_visibility', default=False)

	class Meta:
		ordering = ('date_created', )

	def __str__(self):
		return 'Comment by {} on {}'.format(self.author, self.post)
