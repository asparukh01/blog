from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from ..models import Comment
from ..models import Post
from ..forms import CommentForm


class CommentListView(View):
    template_name = 'comment/comment_list.html'

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        return render(request, self.template_name, {'comments': comments})


class CommentCreateView(LoginRequiredMixin, View):
    template_name = 'post/post_detail.html'

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
            comment = form.save(commit=False)
            comment.post = post
            comment.author = self.request.user
            comment.save()
            return redirect('post_list')
        return render(request, self.template_name, {'form': form})


class CommentDeleteView(LoginRequiredMixin, View):
    template_name = 'post/post_detail.html'

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment.delete()
        return redirect('post_list')
