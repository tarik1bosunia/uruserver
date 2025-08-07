from rest_framework.views import APIView
from rest_framework.response import Response
from ..permissions import IsSuperAdmin, IsStudent

class SuperAdminOnlyView(APIView):
    permission_classes = [IsSuperAdmin]

    def get(self, request):
        return Response({'message': 'Hello SuperAdmin!'})
    

class StudentOnlyView(APIView):
    permission_classes = [IsStudent]

    def get(self, request):
        return Response({'message': 'Hello Student!'})