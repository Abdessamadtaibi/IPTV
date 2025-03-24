from rest_framework import serializers
from . import models

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = ['name','price','description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = ['user_subscription','modepass_subscription','start_date','end_date']
