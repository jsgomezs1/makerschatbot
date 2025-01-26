from rest_framework import serializers, viewsets
from core.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer