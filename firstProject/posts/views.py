from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CreatePostForm

from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {"posts":posts}
    return render(request, 'posts/posts_list.html',context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {"post":post}
    return render(request, 'posts/post.html', context )

@login_required(login_url='users:login')
def post_new(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        print("form.is_valid(): ",form.is_valid())
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            print("request.user: ",request.user)
            post.save()
            # redirect to the previous page
            return redirect('posts:posts_list')
    else:
        form = CreatePostForm()
    context={"form":form}
    return render(request, 'posts/post_new.html',context )

    