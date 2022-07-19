from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..forms import PostForm
from ..models import Post, Category


class PostListView(View):
    template_name = 'post/post_list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts': posts})


class PostCreateView(LoginRequiredMixin, View):
    template_name = 'post/post_create.html'

    def get(self, request, *args, **kwargs):
        form = PostForm()
        statuses = Post.STATUSES
        return render(request, self.template_name, {'form': form, 'statuses': statuses})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect('post_list')
        return render(request, self.template_name, {'form': form})


class PostUpdateView(LoginRequiredMixin, View):
    template_name = 'post/post_update.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        statuses = Post.STATUSES
        form = PostForm(
            initial={
                'title': post.title,
                'image': post.image,
                'link': post.link,
                'status': post.status,
                'category': post.category,
                'text': post.text,

            }
        )
        return render(request, self.template_name, {'post': post, 'form': form, 'statuses': statuses})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        statuses = Post.STATUSES
        if form.is_valid():
            post.title = request.POST.get('title')
            post.image = request.FILES.get('image')
            post.link = request.POST.get('link')
            post.status = request.POST.get('status')
            post.category = get_object_or_404(Category, pk=request.POST.get('category'))
            post.text = request.POST.get('text')
            post.save(update_fields=['title', 'text', 'status', 'image', 'link', 'category'])
            return redirect('post_list')
        return render(request, self.template_name, {
            'form': PostForm(
                initial={
                    'title': post.title,
                    'image': post.image,
                    'link': post.link,
                    'status': post.status,
                    'category': post.category,
                    'text': post.text,
                }),
            'post': post, 'statuses': statuses})


class PostDetailView(View):
    template_name = 'post/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return render(request, self.template_name, {'post': post})


class PostDeleteView(LoginRequiredMixin, View):
    template_name = 'post/post_delete.html'

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        post.delete()
        return redirect('post_list')
