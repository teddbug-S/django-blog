from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Post


# Create your views here.
class HomeView(LoginRequiredMixin, ListView):

    model = Post
    paginate_by = 5
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "Please login to access page.")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserPostsHomeView(HomeView):
    """ Show posts created by a specific user """

    template_name = 'blog/user_posts.html'

    @property
    def user_(self):
        """ Tries to get and return user with username specified in url """
        return get_object_or_404(User, username=self.kwargs.get('username'))
    
    def get_queryset(self):
        # try to get user or return 404 HTTP Response
        user = self.user_
        # return posts by that user
        posts = Post.objects.filter(author__username=user.username).order_by('-date_posted')
        return posts


class IndexView(View):
    """ The about page view """
    
    def get(self, request):
        """ Handles all GET request made to the about page. """
        context = {'title': ''}
        return render(request, template_name='blog/index.html', context=context)


class PostView(View):
    
    def get(self, request, post_id):
        """ Handles all GET request made to the page. """
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            ...
        context = {'title': f'Post | {post.title}', 'post': post}
        return render(request, template_name='blog/home.html', context=context)

