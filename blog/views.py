from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from blog.models import Post

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "bname": "create post",
    }
    return render(request, "blog/Add_post.html", context)

def post(request, id):
    ##instanse = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id = id)
    context = {
        "post": instance,
    }
    return render(request, 'blog/post.html', context)

def post_update(request, id):
    ##instanse = Post.objects.get(id=3)gdfg
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "post": instance,
        "form": form,
        "bname": "edit and save",
    }
    return render(request, 'blog/Add_post.html', context)