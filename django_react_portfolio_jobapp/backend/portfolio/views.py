from rest_framework.views import APIView
from rest_framework.response import Response

class ThemeList(APIView):
    def get(self, request):
        themes = ['netflix', 'amazon', 'microsoft', 'google']
        return Response({'themes': themes})
