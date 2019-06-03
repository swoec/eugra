# Create your views here.


from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserSerializer


# User = get_user_model()


# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
