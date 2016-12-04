#blog/models.py

from django.db import models
from django.utils import timezone

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	subject = models.ForeignKey('Subject', related_name = 'posts', default = 0)
	board = models.ForeignKey('Board', related_name = 'posts', default = 0,)
	problem_num = models.IntegerField(default = 0)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	photo = models.ImageField(default = 0, blank = True, null = True)
	is_deleted = models.BooleanField(default = False)
	hit = models.IntegerField(default = 0)
	like = models.PositiveIntegerField(default = 0)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def num_name(self):
		return str(self.problem_num) + '번'
		
	def name(self):
		return self.board.name() + ' ' + str(self.problem_num) + '번 문제'

	def total_likes(self):
		return self.like.count()

	def __str__(self):
		return self.name()



class Board(models.Model):
	subject = models.ForeignKey('Subject', related_name = 'boards', default = 0)
	year = models.IntegerField(default = 2016)
	semester = models.CharField(max_length = 10)
	quiz_num = models.PositiveIntegerField(default = 1)
	file = models.FileField(default = 0)

	def trans_quiz(self):
		if self.quiz_num == 1:
			return '중간고사'
		elif self.quiz_num == 2:
			return '기말고사'

	def available_prob(self):
		a=[]
		for post in self.posts.all():
			num = post.problem_num
			if num in a:
				continue
			else:
				a.append(num)
		return a

	def best_sol(self):
		a = []
		for num in self.available_prob():
			for post in self.posts.filter(problem_num__exact = num).order_by('-like'):
				if post.is_deleted == False:
					a.append(post)
					break
		return a


	def name(self):
		return str(self.year)+'학년도 '+str(self.semester)+'학기 '+self.trans_quiz()

	def __str__(self):
		return self.name()

class Subject(models.Model):
	subject_name = models.CharField(max_length = 30)
	subject_code = models.CharField(max_length = 20)

	def __str__(self):
		return self.subject_name


'''
class ImageExample(models.Model):
	image = ProcessedImageField(
		upload_to = _generate_upload_path,
		processors = [ResizeToFill(100,50)],
		format='JPEG'
		options = {'quality' : 60}

	)
'''

'''
class Upload(models.Model):
	title = models.CharField(max_length = 100)
	photo = models.ImageField()
'''


