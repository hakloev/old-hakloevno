from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Blogpost, Category
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_posts(request):
    context = {}
    context['request'] = request
    context['categories'] = Category.objects.all()
    context['posts'] = Blogpost.objects.all().order_by('-posted')
    return render(request, u'blog/blog.html', context)

@login_required
def create_post(request):
    context = {}
    if request.method == "POST":
        errors = []
        c = Category.objects.latest('title')
        if not request.POST.get('title', ''):
            errors.append('Legg inn tittel')
        if not request.POST.get('ingress', ''):
            errors.append('Legg inn ingress')
        if not request.POST.get('text', ''):
            errors.append('Legg inn innhold')
        else:
            context['text'] = request.POST['text']
        if not errors:
            b = Blogpost(title=request.POST['title'], ingress=request.POST['ingress'], text=request.POST['text'], category=c)
            b.save()
            return HttpResponseRedirect(b.get_absolute_url())
        else:
            context['errors'] = errors
    else:
        context['request'] = request
        context['categories'] = Category.objects.all()
    return render(request, u'blog/newpost.html', context)

def post_by_slug(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    context = {}
    context['post'] = post
    context['request'] = request
    return render(request, u'blog/article.html', context)
