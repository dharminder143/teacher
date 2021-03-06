from rest_framework.serializers import ModelSerializer
from user.models import User 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    teacher= serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        fields = ('id', 
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'groups',
            'password',
            'instrument',
            'since',
            'date_of_birth',
            'skill',
            'teacher')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
