from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from apps.blog.models import Blogpost, Category
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
        if not request.POST.get('title', ''):
            errors.append('Legg inn tittel')
        if not request.POST.get('ingress', ''):
            errors.append('Legg inn ingress')
        if not request.POST.get('text', ''):
            errors.append('Legg inn innhold')
        else:
            context['text'] = request.POST['text']
        if not errors:
            try:
                b = Blogpost.objects.get(title=request.POST['title'])
                b.ingress = request.POST['ingress']
                b.text = request.POST['text']
                b.save()
            except:
                b = Blogpost(title=request.POST['title'], ingress=request.POST['ingress'], text=request.POST['text'])
                b.save()
            return HttpResponseRedirect(b.get_absolute_url())
        else:
            context['errors'] = errors
    else:
        context['request'] = request
        context['categories'] = Category.objects.all()
    return render(request, u'blog/newpost.html', context)

def post_by_year(request, year):
    posts = Blogpost.objects.filter(posted__year=int(year)).order_by('-posted')
    return render(request, u'blog/blog.html', {'request': request, 'posts': posts})

def post_by_month(request, year, month):
    posts = Blogpost.objects.filter(posted__year=int(year), posted__month=int(month)).order_by('-posted')
    return render(request, u'blog/blog.html', {'request': request, 'posts': posts})

def post_by_day(request, year, month, day):
    posts = Blogpost.objects.filter(posted__year=int(year), posted__month=int(month), posted__day=int(day)).order_by('-posted')
    return render(request, u'blog/blog.html', {'request': request, 'posts': posts})

def post_by_slug(request, year, month, day, slug):
    s = '/%s/%s/%s/%s' % (year, month, day, slug)
    post = get_object_or_404(Blogpost, slug=s)
    return render(request, u'blog/article.html', {'request': request, 'post': post})