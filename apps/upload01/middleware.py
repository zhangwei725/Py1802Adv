from django.utils.deprecation import MiddlewareMixin


class MD(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        print(request)

    def process_view(self, request):
        print(request)

    def process_response(self, request, response):
        print('process_response')
        return response
