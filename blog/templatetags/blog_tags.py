from django import template
from ..models import Post, Category

register = template.Library()


@register.inclusion_tag("blog/blog-popular.html")
def latestpost(arg=3):
    posts = Post.objects.filter(status=True).order_by("-published_date")[:arg]
    return {"posts": posts}


@register.inclusion_tag("blog/blog-category.html")
def categoriespost():
    posts = Post.objects.filter(status=True).order_by("-published_date")
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        post_count = posts.filter(category=cat).count()
        cat_dict[cat] = post_count
    return {"categories": cat_dict}