from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    '''
    Viewlar yerine viewsetler kullanarak apimizin otomatik olarak url configrasyinu yapmasini sagladik. Bunu da router 
    class imiza viewsetimize kaydederek basardik.
    
    Son olarak varsayilan giris ve cikis viewlarimizi taranabilir api ile birlikte kullanmak icin dahil ediyoruz. Bu
    istege bagli ancak kullanislidir. Eger api iniz kimlik dogrulamasi gerektiriyorsa ve yinede taranabilir api 
    kullanmak istiyorsaniz ..
    '''

