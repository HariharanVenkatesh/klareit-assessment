from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Busapp
from .serializers import BusappSerializer

@api_view(['GET'])
def search_buses(request):
    source = request.GET.get('source')
    destination = request.GET.get('destination')

    if not source or not destination:
        return Response(
            {"error": "Source and Destination are Required"},
            status=400
        )
    
    buses = Busapp.objects.filter(
        source__iexact=source,
        destination__iexact=destination
    )

    serializer = BusappSerializer(buses, many=True)

    return Response({
        "source": source,
        "destination": destination,
        "available_buses": serializer.data
    })

