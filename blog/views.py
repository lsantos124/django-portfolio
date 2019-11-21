from django.shortcuts import render, get_object_or_404

from .models import Blog

def getblogs(request):
	blogs = Blog.objects
	categories = ["Travel", "Technology", "Books"]
	return render(request, 'blog/blogs.html', {"blogs":blogs, "categories":categories})

def detail(request, blog_id):
	detailedblog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {"blog":detailedblog})

def getBlogsFromCategory(request, cat):
	blogs = Blog.objects.all().filter(category=cat)
	categories = ["Travel", "Technology", "Books"]
	return render(request, 'blog/blogs.html', {"blogs":blogs, "categories":categories})