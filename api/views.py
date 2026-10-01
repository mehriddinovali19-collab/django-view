from django.views import View
from django.http import HttpResponse, HttpRequest

class ItemView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("get method called")

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("post method called")

    def delete(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("delete method called")

    def put(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("put method called")

