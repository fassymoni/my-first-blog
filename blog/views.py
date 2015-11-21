from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
	posts = Post.objects.all().order_by('title')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	print(pk)
	post = get_object_or_404(Post, pk=pk)
	#post=Post.objects.get(id=pk)
	return render(request, 'blog/post_detail.html', {'post': post})