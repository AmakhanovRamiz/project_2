from rest_framework import generics

from .models import Advert
from .serializers import AdvertSer


class AdvertList(generics.ListAPIView):
    """Все объявления"""
    permission_classes = [permission]
    queryset = Advert.objects.all()
    serializer_class = AdverSer


# class AdvertDetail(DetailView):
#     """Подробное об объявлении"""
#     model = Advert
#     context_object_name = 'advert'
#     template_name = 'notice_board/advert-detail.html'
   
    