from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from apps.blog.models import Blogpost, Category
from django.core.urlresolvers import reverse
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
            return HttpResponseRedirect(
                reverse('blog:post_by_slug', 
                    kwargs={'year': b.posted.year, 
                            'month': b.posted.month, 
                            'day': b.posted.day, 
                            'slug': slugify(b.title)
                    }
                )
            )
        else:
            context['errors'] = errors
    else:
        context['request'] = request
        context['categories'] = Category.objects.all()
    return render(request, u'blog/newpost.html', context)

def post_by_year(request, year):
    context = {'request': request}
    posts = Blogpost.objects.filter(posted__year=int(year)).order_by('-posted')
    context['posts'] = posts
    context['categories'] = Category.objects.all()
    return render(request, u'blog/blog.html', context)

def post_by_month(request, year, month):
    context = {'request': request}
    posts = Blogpost.objects.filter(posted__year=int(year), posted__month=int(month)).order_by('-posted')
    context['posts'] = posts
    context['categories'] = Category.objects.all()
    return render(request, u'blog/blog.html', context)

def post_by_day(request, year, month, day):
    context = {'request': request}
    posts = Blogpost.objects.filter(posted__year=int(year), posted__month=int(month), posted__day=int(day)).order_by('-posted')
    context['posts'] = posts
    context['categories'] = Category.objects.all()
    return render(request, u'blog/blog.html', context)

def post_by_slug(request, year, month, day, slug):
    context = {'request': request}
    s = '/%s/%s/%s/%s' % (year, month, day, slug)
    post = get_object_or_404(Blogpost, slug=s)
    context['post'] = post
    context['categories'] = Category.objects.all()
    return render(request, u'blog/article.html', context)

def category_by_slug(request, category):
    posts = Blogpost.objects.all().order_by('-posted')
    category_posts = [post for post in posts if post.categories.filter(slug=category)]
    return render(request, u'blog/category.html', {
        'request': request,
        'category': category,
        'posts': category_posts })

