from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog
from django.template import loader


# Create your views here.
def index(request):
    all_blogs = Blog.objects.all()
    template = loader.get_template("blogs/index.html")
    context = {
        "all_blogs": all_blogs,
    }
    return HttpResponse(template.render(context, request))

def detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, "blogs/detail.html", {"blog": blog})
