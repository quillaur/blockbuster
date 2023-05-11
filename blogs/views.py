from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic


class IndexView(generic.ListView):
    template_name = "blogs/index.html"
    context_object_name = "all_blogs"

    def get_queryset(self):
        """Return all blog articles."""
        return Blog.objects.all()

# Create your views here.
# def index(request):
#     all_blogs = Blog.objects.all()
#     template = loader.get_template("blogs/index.html")
#     context = {
#         "all_blogs": all_blogs,
#     }
#     return HttpResponse(template.render(context, request))


def detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    
    if request.method == "POST":
        blog.title = request.POST["blog_title"]
        blog.body = request.POST["blog_body"]
        blog.save()

    return render(request, "blogs/detail.html", {"blog": blog})

def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, "blogs/blog_update.html", {"blog": blog})