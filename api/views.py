from api import alchemy, models, serializers
import itertools
from concurrent.futures import ThreadPoolExecutor
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, decorators

# settings
blockTransactionDetail = False


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EthBlockViewSet(viewsets.ModelViewSet):
    """
    TODO
    """
    queryset = models.EthBlock.objects.all()
    api = alchemy.EthApiClass()
    model = models.EthBlock
    serializer_class = serializers.EthBlockSerializer

    def saveBlock(self, response: dict):
        smartblock = self.model(
            number=response['number'],
            hash=response['hash'],
            timestamp=response['timestamp'],
            transactions=response['transactions']
        )
        smartblock.save()

    @decorators.action(detail=False)
    def cache_blocks(self, request):
        latest_number = self.api.getNumber()
        try:
            latest_object = self.model.objects.first().number
            if int(latest_number, 16) - int(latest_object, 16) > 128:
                raise ValueError
        except (AttributeError, ValueError) as e:  # notExistsObject or tooManyObject
            response = self.api.getFormatBlock(latest_number, blockTransactionDetail)
            self.saveBlock(response)
            return JsonResponse({'process': f'{self}', 'error': e.__class__.__name__, 'count': 1, 'latest_number': latest_number})

        rge = [hex(x) for x in range(int(latest_object, 16) + 1, int(latest_number, 16) + 1)]
        with ThreadPoolExecutor() as executor:
            responses = executor.map(self.api.getFormatBlock, rge, itertools.repeat(blockTransactionDetail))
        for response in responses:
            self.saveBlock(response)
        return JsonResponse({'process': f'{self}', 'count': len(rge), 'latest_number': latest_number, 'latest_object': latest_object})
