from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from ..serializers import UserCreateSerializer


class ItemView(APIView):
    def get(self, request: Request) -> Response:
        search  = request.query_params.get('search')
        limit  = request.query_params.get('limit')
        print(search, limit)
        return Response("get method called")

    def post(self, request: Request) -> Response:
        data = request.data
        print(data)
        return Response("post method called")

    def delete(self, request: Request) -> Response:
        return Response("delete method called")

    def put(self, request: Request) -> Response:
        return Response("put method called")



class UserCreateView(APIView):
    def post(self, request: Request) -> Response:
       serializer = UserCreateSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       return Response(serializer.validated_data)