from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from IPTV_api.models import Plan, Subscription

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ['home', 'login', 'register','payments']

    def location(self, item):
        return reverse(item)

class PlanSitemap(Sitemap):
    """Sitemap for available IPTV plans"""
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Plan.objects.all()

    def location(self, obj):
        return f"/plan/{obj.id}/"  # Assuming each plan has a detail page
