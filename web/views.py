from django.shortcuts import render,get_object_or_404
from django.http.response import  HttpResponse

from posts.models import Post,Author, Category
from main.functions import paginate_instances


def index(request):
    posts = Post.objects.filter(is_deleted=False,is_draft=False)

    categories =Category.objects.all()[:6]
    authors =Author.objects.all()

    q = request.GET.get('q')
    if q:
        posts= posts.filter(title__icontains=q)
        # i use cheyyumpol caseinsensetive aayi search work cheyyunuu
        # posts= posts.filter(title__istartswith=q)
        # posts= posts.filter(title__iendswith=q)

    search_authors = request.GET.getlist("author")
    if search_authors:
        posts=posts.filter(author__in=search_authors)
    
    search_categories = request.GET.getlist("category")
    if search_categories:
        posts=posts.filter(categories__in=search_categories).distinct()

    sort=request.GET.get("sort")
    if sort:
        if sort == "title-asc":
            posts =posts.order_by("title")
        elif sort == "title-desc":
            posts =posts.order_by("-title")
        elif sort == "date-asc":
            posts =posts.order_by("published_date")
        elif sort == "date-desc":
            posts =posts.order_by("-published_date")



    instances = paginate_instances(request, posts)
    # instances = paginate_instances(request, posts,per_page=3)

    context = {
        "title": "Home PAGE ",
        "instances": instances,
        "categories": categories,
        "authors":authors

    }
    return render(request,'web/index.html',context=context)

def post(request,id):
    instance = get_object_or_404(Post.objects.filter(id=id))
    context={
        "instance" : instance
    }
    return render(request,'web/post.html',context=context)
