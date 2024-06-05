from blog.models import Post
from django.views.generic import ListView,DetailView
# Create your views here.


class BlogListView(ListView):
    paginate_by = 9
    model = Post
    template_name = "blog/blog.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog-detail.html"
