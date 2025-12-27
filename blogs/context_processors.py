from .models import Category
from assignment.models import SocialLink
from django.db.models import Count

def get_categories(request):
    categories = Category.objects.all().order_by('-updated_at')
    sidebar_categories = (
        Category.objects
        .annotate(blog_count=Count('blog'))
        .filter(blog_count__gte=1)  # only categories with at least 1 blog
        .order_by('-blog_count')     # optional: order by most blogs first
    )
    topbar_categories = (
        Category.objects
        .annotate(blog_count=Count('blog'))
        .order_by('-blog_count')[:4]
    )
    return {
        'categories': categories,
        'topbar_categories': topbar_categories,
        'sidebar_categories' : sidebar_categories,
    }


def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)