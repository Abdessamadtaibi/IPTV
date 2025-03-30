from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from IPTV_api.models import Plan, Subscription

class StaticViewSitemap(Sitemap):
    protocol = 'https' 
    def items(self):
        return ['home','plans']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == 'home' else 0.6

    def changefreq(self, item):
        return "weekly" if item == 'home' else "yearly"


class PlanSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"  # Adjust based on update frequency

    def items(self):
        return Plan.objects.all()

    def location(self, obj):
        return reverse('pay',args=[obj.slug])  # Use URL name

