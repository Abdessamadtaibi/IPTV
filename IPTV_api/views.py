from django.shortcuts import render,get_object_or_404,redirect
from .models import Plan,Subscription,Payment
from rest_framework.decorators import APIView
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser ,IsAuthenticated,AllowAny
from django.contrib.auth.models import User,Group
from django.http import JsonResponse,HttpResponse
from django.views.generic import TemplateView
from rest_framework import exceptions
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf import settings
from rest_framework.authtoken.models import Token

def registerview(request):
    return render(request,'register.html')

def loginview(request):
    return render(request,'login.html')

def homeview(request):
    seo_data = {
        "title": "Best IPTV Subscription - HD Streaming & Fast Servers",
        "description": "Get the best IPTV subscription with HD channels, fast servers, and affordable pricing.",
        "keywords": "best IPTV, IPTV subscription, HD IPTV, IPTV for Firestick"
    }
    plans = Plan.objects.all()
    return render(request,'home.html',seo_data,)

def userview(request):
    return render(request,'user.html',)


def robots_txt(request):
    content = """User-agent: *
Disallow: /admin/
Disallow: /user/
Disallow: /api/
Disallow: /auth/
Sitemap: /sitemap.xml/
"""
    return HttpResponse(content, content_type="text/plain")

def pay(request,slug=None):
    if slug :
        plan = get_object_or_404(Plan,slug=slug)
        return render(request,'pay.html',{'plan':plan})

def plans(request):
        plans = Plan.objects.all()
        return render(request,'plans.html',{'plans':plans})

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        subscription = Subscription.objects.get(user=request.user)
        serializer = serializers.UserSerializer(subscription)
        return Response(serializer.data)
