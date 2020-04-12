from rest_framework import generics
from rest_framework import permissions

from backend.notice_board.models import Advert 
from backend.notice_board.serializers import AdvertListSer, AdvertCreateSer


from .models import Profile
from .serializers import ProfileSer, ProfileUpdateSer

class ProfileDetail(generics.RetrieveAPIView):
    """Профиль пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer

class ProfileUpdateView(generics.UpdateAPIView):
    """Редактирование профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer

class UserAdvertList(generics.ListAPIView):
    """Все объявления пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertListSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)
    
class UserAdvertUpdate(generics.UpdateAPIView):
    """Все объявления пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertCreateSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)