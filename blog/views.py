from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ( 
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse

def home(request):
    context = {
        'posts': Post.objects.all(),
        'latest_posts': Post.objects.order_by('-date_posted')[:5] 
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Newest to oldest
    paginate_by = 6  # 6 posts per page 

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6  # 6 posts per page 

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        # Get the context from the parent class
        context = super().get_context_data(**kwargs)
        # Get the page object (paginated posts)
        page_obj = context['page_obj']
        # Add animation delay to each post on the current page
        for i, post in enumerate(page_obj):
            post.animation_delay = i * 0.1  # 0.1s increment per post (0.0s, 0.1s, 0.2s, 0.3s)
        return context

class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 6  # 6 posts per page 

    def get_queryset(self):
        self.category = self.kwargs.get('category')
        if self.category == 'all':
            return Post.objects.all().order_by('-date_posted')
        return Post.objects.filter(category=self.category).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-date_posted')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=self.object.pk)
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
@require_POST
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return JsonResponse({
        'status': 'ok',
        'liked': post.likes.filter(id=request.user.id).exists(),
        'total_likes': post.total_likes()
    })

@login_required
@require_POST
def bookmark_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return JsonResponse({
        'status': 'ok',
        'bookmarked': post.bookmarks.filter(id=request.user.id).exists(),
        'total_bookmarks': post.total_bookmarks()
    })

class LikedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/liked_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(likes=self.request.user).order_by('-date_posted')

class BookmarkedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/bookmarked_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(bookmarks=self.request.user).order_by('-date_posted')