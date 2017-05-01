from django import forms


from .models import Post,Board
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = {'title', 'text', 'photo', 'problem_num'}


class BoardForm(forms.ModelForm):

	class Meta:
		model = Board
		fields = {'year', 'semester', 'quiz_num', 'file'}

'''
class UserForm(forms.ModelForm):

	reg_username = models.CharField(max_length = 10)
	reg_password = models.CharField(max_length = 10)
	reg_password_confirm = models.CharField(max_length = 10)
	reg_email = models.CharField(max_length = 30)
	reg_firstname = models.CharField(max_length = 10)
	reg_lastname = models.CharField(max_length = 10)
	reg_gender = models.CharField(max_length = 10)
	'''

'''
class UploadForm(forms.ModelForm):

	class Meta:
		model = UploadForm
		fields = {'title', 'photo',}

'''
