#blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Subject, Board
from django.utils import timezone
from .forms import PostForm, BoardForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def main_page(request):
	return render(request, 'blog/main_page.html')

def solution_list(request,pk):
	problem = get_object_or_404(Problem, pk=pk)
	solutions = problem.solutions.all().order_by('like')
	return render(request, 'blog/solution_list.html', {'solutions' : solutions})

def problem_list(request,pk):
	board = get_object_or_404(Board,pk=pk)
	problems = board.problems.all().order_by('problem_num')
	return render(request, 'blog/problem_list.html', {'problems' : problems})

def board_view(request, pk):
	board = get_object_or_404(Board, pk=pk)
	posts = board.best_sol()
	return render(request, 'blog/board_view.html', {'posts' : posts , 'board' : board, 'subject' : board.subject})

def isCode(keyword):
	return keyword[:2] == "CS" or keyword[:3] == "MAS"

def board_list(request,pk):
	subject = get_object_or_404(Subject,pk=pk)
	boards = subject.boards.all().order_by('year','semester','quiz_num')
	return render(request, 'blog/board_list.html', {'boards' : boards, 'subject' : subject})

def search(request):
	if request.method == "POST":
		form = request.POST
		keyword = form.get('keyword')
		if isCode(keyword):
			subject = Subject.objects.filter(subject_code__icontains = keyword)
		else:
			subject = Subject.objects.filter(subject_name__icontains = keyword)
		return render(request, 'blog/search_result.html', {'subject' : subject})
	else:
		form = {};
	return render(request,'blog/main_page.html', {'form': form})

def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            print("unlike")
            if post.like > 0:
                likes = post.like - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+post_id] = True
            likes = post.like + 1
    post.like = likes
    post.save()
    return HttpResponse(likes, liked)

def get_like(request):
	cat_id = None
	liked = False
	if request.method == 'GET':
		cat_id = request.GET['category_id']
		likes = 0
		if cat_id:
			cat = Post.objects.get(id=int(cat_id))
			if cat:
				likes = cat.like + 1
				liked = True
				cat.like =  likes
				cat.save()
				return HttpResponse(likes, liked)

@login_required
def like_category(request):

    cat_id = None
    if request.method == 'GET':
    	cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)

@login_required
def post_list(request,pk):
	post = get_object_or_404(Post,pk=pk)
	posts = Post.objects.filter(board__exact = post.board, problem_num__exact=post.problem_num).order_by('-like')
	return render(request, 'blog/post_list.html', {'posts' : posts, 'num' : post.num_name(), 'board' : post.board })

@login_required
def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post_id = post.pk
	liked = False
	if request.session.get('has_liked_'+str(post_id), liked):
		liked = True
		print("liked {}_{}".format(liked, post_id))
	post.hit+=1
	post.save()
	return render(request, 'blog/post_detail.html', {'post' : post, 'board' : post.board, 'liked' : liked })

@login_required
def post_delete(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.is_deleted = True
	post.save()
	return redirect('post_list', pk=post.pk)

@login_required
def post_new(request, pk):
	board = get_object_or_404(Board,pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES) 
		if form.is_valid():
			post = form.save(commit=False)
			post.subject = board.subject
			post.board = board
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def board_new(request, pk):
	subject = get_object_or_404(Subject, pk=pk)
	if request.method == "POST":
		form = BoardForm(request.POST, request.FILES) 
		if form.is_valid():
			board = form.save(commit=False)
			board.subject = subject
			board.save()
			return redirect('board_view', pk=board.pk)
	else:
		form = BoardForm()
	return render(request, 'blog/board_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def register(request):
	if request.method == "POST":
		form = request.POST
		user = User.objects.create_user(form.get('reg_username'), form.get('reg_email'), form.get('reg_password'))
		user.last_name = form.get('reg_lastname')
		user.first_name = form.get('reg_firstname')
		user.save()
		return redirect('/')
	else:
		form = {};
	return render(request,'registration/register.html', {'form': form})

'''
def upload_new(request):
	if request.method == "POST":
		form = UploadForm(request.POST) 
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = UploadForm()
	return render(request, 'blog/post_edit.html', {'form' : form})
'''
