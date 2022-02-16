from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') #.order_by('-pk') 최신이 맨위로 정렬

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post=Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )