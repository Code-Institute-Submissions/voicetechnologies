from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm


# Create your views here.
def get_posts(request):
    posts = Post.objects.order_by('-published_date')

    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    comments = post.comments.filter(active=False)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "postdetail.html",
                  {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
