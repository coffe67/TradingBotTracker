from rest_framework.response import Response
from rest_framework.views import APIView


class BotView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)  # Log the incoming request data
        return Response({"message": "Hello, World!"})
