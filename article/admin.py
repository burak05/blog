from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date","category"]
    list_display_links = ["title","author","created_date","category"]
    search_fields = ["category"]
    list_filter = ["category"]
    class Meta:
        model = Article