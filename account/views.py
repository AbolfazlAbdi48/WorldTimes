from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from news.models import Comment
from .forms import RegisterForm
from .models import User


# Create your views here.


class RegisterView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    form_class = RegisterForm


class AccountDetailView(LoginRequiredMixin, DetailView):
    def get_object(self, queryset=None):
        return User.objects.filter(id=self.request.user.id).first()

    template_name = 'registration/account.html'


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    def get_object(self, queryset=None):
        return User.objects.filter(id=self.request.user.id).first()

    success_url = reverse_lazy('account:home')
    fields = ('username', 'email', 'first_name', 'last_name')
    template_name = 'registration/account-update.html'


class CommentListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Comment.objects.filter(owner=self.request.user).order_by('-id')

    template_name = 'registration/account-comment-list.html'


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    def get_object(self, queryset=None):
        comment_id = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, owner=self.request.user, id=comment_id)

        return comment

    template_name = 'registration/account-comment-update.html'
    fields = ('text',)
    success_url = reverse_lazy('account:comments')


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    def get_object(self, queryset=None):
        comment_id = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, owner=self.request.user, id=comment_id)

        return comment

    template_name = 'registration/account-comment-delete.html'
    success_url = reverse_lazy('account:comments')
