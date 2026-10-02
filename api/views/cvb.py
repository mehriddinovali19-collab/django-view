from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request



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

