from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from sblog.models import *
from sblog.forms import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def errorpage(request):
    return render_to_response("500.html",
        context_instance=RequestContext(request)
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #if new_user is not None and new_user.is_active:
            #    auth.login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html",
        {'form': form,},
        context_instance=RequestContext(request)
    )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/")
    else:
       return render_to_response("registration/register.html",
           context_instance=RequestContext(request))

def logout(request):
    try:
        auth.logout(request)
        return HttpResponseRedirect("/")
    except KeyError:
        pass
    return render_to_response("blog_list.html",
        context_instance=RequestContext(request))

def user(request, id=''):
    tags = Tag.objects.all()
    user = User.objects.get(id=id)
    blogs = user.blog_set.all()
    for blog in blogs:
        comments = blog.comment_set.all()
        blog.com_count = comments.count()

    return render_to_response("registration/user.html",
        {"blogs": blogs, "tags": tags},
        context_instance=RequestContext(request))

def blog_list(request):
    blogs = Blog.objects.order_by('-publish_time')
    tags = Tag.objects.all()
    comments = [];
    for blog in blogs:
        comments = blog.comment_set.all()
        blog.com_count = comments.count()

    return render_to_response("blog_list.html", 
        {"blogs": blogs,"tags": tags,"comments":comments},
        context_instance=RequestContext(request),)

def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    for blog in blogs:
        comments = blog.comment_set.all()
        blog.com_count = comments.count()

    return render_to_response("blog_filter.html",
        {"blogs": blogs, "tag": tag, "tags": tags},
        context_instance=RequestContext(request))

def blog_search(request):
    tags = Tag.objects.all()
    if request.method == 'GET':
        if 'search' in request.GET:
            search_str=request.GET['search']
            blogs=Blog.objects.filter(caption__icontains=search_str).order_by('-id')
            for blog in blogs:
                comments = blog.comment_set.all()
                blog.com_count = comments.count()

            return render_to_response("blog_search.html",
                {"blogs": blogs, "tags": tags},
                context_instance=RequestContext(request))
    else:
        return render_to_response("/",
            context_instance=RequestContext(request))

def blog_show(request, id=''):
    try:
        blogs = Blog.objects.order_by('-id')
        blog = Blog.objects.get(id=id)
        tags = Tag.objects.all()
        comments = blog.comment_set.all()
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",
        {"blogs": blogs,"blog": blog, "tags": tags, "comments": comments},
        context_instance=RequestContext(request))

def blog_add(request):
    blogs = Blog.objects.order_by('-id')
    tags = Tag.objects.all()
    if request.method == 'POST':
        caption = request.POST['caption']
        content = request.POST['content']
        tag_id = request.POST['tagRadios']
        tag = Tag.objects.get(id=tag_id)
        user = request.user
        blog = Blog(user=user,caption=caption, content=content,tag=tag)
        blog.save()
        id = Blog.objects.order_by('-id')[0].id
        return HttpResponseRedirect('/blog/%s' % id)
    else:
        pass
    return render_to_response('blog_add.html',{"blogs": blogs,"tags": tags},
        context_instance=RequestContext(request))

def comment_add(request):
    blogs = Blog.objects.order_by('-id')
    tags = Tag.objects.all()
    if request.method == 'POST':
        content = request.POST['comment']
        blog_id = request.POST['blog_id']
        blog = Blog.objects.get(id=blog_id)
        user = request.user
        comment = Comment(user=user,blog=blog, content=content)
        comment.save()
        return HttpResponseRedirect('/blog/%s' % blog_id)
    else:
        pass
    return render_to_response('blog_add.html',{"blogs": blogs,"tags": tags},
        context_instance=RequestContext(request))

