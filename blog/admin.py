#blog/admin.py

from django.contrib import admin
from .models import Post, Board, Subject


# Register your models here.



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'subject_name']
    list_display_links = ['subject_name']

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
	fields = ['subject' , 'year', 'semester', 'quiz_num', 'file']
	list_display = ['year', 'semester', 'quiz_num', 'subject_name']
	list_display_links = ['quiz_num']

	def subject_name(self, instance):
		return instance.subject.subject_name

admin.site.register(Post)

'''
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
	fields = ['subject', 'board', 'problem_num', 'photo', 'file']
	list_display = ['problem_num']
	list_display_links = ['problem_num']

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
	fields = ['subject', 'board', 'problem', 'title', 'photo', 'file']
	list_display = ['title']
	list_display_links = ['title']
'''