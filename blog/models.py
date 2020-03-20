from django.db import models 
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# class Comment(models.Model):
# 	post = models.ForeignKey('post', related_name='comments')
# 	author = modelsCharField(max_length=200)
# 	text = models.TexField()
# 	created_date = models.DateTimeField(default=timezonenow)
# 	approved_comment = modelsBooleanField(default=False)

	# def approve(self):
	# 	self.approved_comment = True
	# 	self.save('enter code here')

	# def __str__(self):
	#    return self.text	