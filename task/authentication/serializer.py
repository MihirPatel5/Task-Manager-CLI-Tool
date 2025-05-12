from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    class Meta:
        model = Task
        fields = ['id', 'name','description', 'created_at', 'due_date', 'status', 'assgined_to']
        read_only_fields =['id', 'created_at']
