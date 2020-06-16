from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here.
def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})
