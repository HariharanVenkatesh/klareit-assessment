from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BusApp

class BusappAPI(APIView):
    def post(self, request):
        
        print("Request Data:", request.data)
        
        
        return Response({"message": "API is Ready"})
