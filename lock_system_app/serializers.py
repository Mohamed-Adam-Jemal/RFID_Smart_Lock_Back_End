from rest_framework import serializers
from .models import RFIDUser, AccessLog

class RFIDUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFIDUser
        fields = '__all__'

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = '__all__'

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = '__all__'
    
