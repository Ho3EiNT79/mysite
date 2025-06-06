from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post

# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context=context)


def blog_single(request, pid):
    post = get_object_or_404(
        Post, id=pid, status=True, published_date__lte=timezone.now()
    )
    
    post.counted_views += 1
    post.save(update_fields=["counted_views"])
    
    all_posts = list(Post.objects.filter(status=True, published_date__lte=timezone.now()))
    now_post = next((i for i, p in enumerate(all_posts) if p.pk == post.pk), None)
    
    previous_post = all_posts[now_post - 1] if now_post > 0 else None
    next_post = all_posts[now_post + 1] if now_post < len(all_posts) - 1 else None
    
    
    context = {
        "post": post,
        "previous_post": previous_post,
        "next_post": next_post
    }
    return render(request, "blog/blog-single.html", context=context)
    