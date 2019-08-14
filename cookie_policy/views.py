from rest_framework.response import Response
from rest_framework.decorators import (
    api_view, permission_classes, throttle_classes
)
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import AcceptRecord
from .info import get_client_ip


@api_view(['GET'])
@permission_classes([])
@throttle_classes([UserRateThrottle, AnonRateThrottle])
def accept(request):
    user = None if request.user.is_anonymous else request.user
    AcceptRecord.objects.create(
        ip=get_client_ip(request),
        user=user,
    )
    request.session['accepted_cookie_policy'] = True
    return Response(status=204)
