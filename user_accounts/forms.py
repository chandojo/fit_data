from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BlogAuthor


class BlogAuthorCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = BlogAuthor
        fields = ('email', 'name')


class BlogAuthorChangeForm(UserChangeForm):

    class Meta:
        model = BlogAuthor
        fields = ('email', 'name', 'bio', 'prof_img')
