from django.shortcuts import render,get_object_or_404
from .models import BlogPost
from django.core.paginator import Paginator,EmptyPage


def blog_index(request):
    posts = BlogPost.objects.all()
    title_query = request.GET.get('title')
    if title_query:
        posts = posts.filter(title__icontains=title_query)
    paginator = Paginator(posts,per_page=4)
    page_number = request.GET.get('page',default=1)
    page_obj = paginator.get_page(page_number)
    try:
            posts = paginator.page(number=page_number)
    except EmptyPage:
            return 0
    return render(request, "blog/index.html", {'posts':posts,'page_obj': page_obj,'title_query': title_query,})

def blog_detail(request,slug=None):
    if slug :
     post = get_object_or_404(BlogPost,slug=slug)
    return render(request,'blog/detail.html',{'post':post})
