from django.views import View
from django.http import HttpResponse, HttpRequest

def item_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse("get method called")
    if request.method == 'POST':
            return HttpResponse("get method called")
    if request.method == 'DELETE':
            return HttpResponse("get method called")
    if request.method == 'PUT':
            return HttpResponse("get method called")
    else:
         return HttpResponse(
              "PAGE NOT FOUNDED!"
         )
