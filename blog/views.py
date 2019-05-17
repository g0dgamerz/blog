from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
	model=Post
	template_name="index.html"


class PostDetail(generic.DetailView):
	model=Post
	template_name='post_detail.html'
