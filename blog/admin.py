from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title", "status", "counted_views", "published_date")
    search_fields = ["title", "content"]
    list_filter = ("status",)
    # ordering = ["-created_date"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
