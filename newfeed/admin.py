from django.contrib import admin
from .models import Post_content, Comment

class CommentInline(admin.StackedInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by','content', 'time_create']
    list_filter = ['time_create']
    inlines = [CommentInline]
    search_fields = ['id', 'time_create']
    
admin.site.register(Post_content, PostAdmin)
