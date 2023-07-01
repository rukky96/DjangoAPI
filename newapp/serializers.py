from rest_framework import serializers
from .models import Subscriber
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['username', 'email', 'first_name', 'last_name', 'location', 'dvg_points', 'wallet_amount']
        

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators = [UniqueValidator(queryset=Subscriber.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )
 
 
    class Meta:
        model = Subscriber
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2', 'transaction_pin',  'location']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'transaction_pin': {'required': True, 'write_only':True},
        }
    
    def create(self, validated_data):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."}
            )
        return attrs
    def create(self, validated_data):
        subscriber = Subscriber.objects.create(
            username=validated_data['username'],
            email=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            location=validated_data['location'],
            transaction_pin=['transaction_pin']
        )
        subscriber.set_password(validated_data['password'])
        subscriber.save()
        return subscriber

    
    