from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import BlogAuthorCreationForm, BlogAuthorChangeForm
from .models import BlogAuthor


class BlogAuthorAdmin(UserAdmin):
    add_form = BlogAuthorCreationForm
    form = BlogAuthorChangeForm
    model = BlogAuthor
    list_display = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Author Info', {'fields': ('name', 'bio', 'prof_img')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'name')
    ordering = ('email', 'name')


admin.site.register(BlogAuthor, BlogAuthorAdmin)
