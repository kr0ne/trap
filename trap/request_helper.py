import re
import collections
from django.utils import timezone


class CurrentRequest:
    def __init__(self, request):
        self.req_time = self.get_current_time()
        self.rem_ip = self.get_rem_ip_address(request)
        self.req_method = self.get_request_method(request)
        self.scheme = self.get_request_scheme(request)
        self.query_string = self.get_query_string(request)
        self.query_parameters = self.get_query_parameters(request)
        self.cookies = self.get_cookies(request)
        self.headers = self.get_request_headers(request)

    def get_query_parameters(self, request):
        query_parameters = {}
        if request.POST:
            post_dict = request.POST.dict()
            converted_dict = self.convert(post_dict)
            query_parameters["Post parameters"] = converted_dict
        if request.GET:
            get_dict = request.GET.dict()
            converted_dict = self.convert(get_dict)
            query_parameters["Get parameters"] = converted_dict
        return query_parameters

    def convert(self, data):
        if isinstance(data, basestring):
            return str(data)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.convert, data.iteritems()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.convert, data))
        else:
            return data

    @staticmethod
    def get_current_time():
        current_time = timezone.now()
        return current_time

    @staticmethod
    def get_rem_ip_address(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    @staticmethod
    def get_request_method(request):
        return request.method

    @staticmethod
    def get_request_scheme(request):
        return request.scheme

    @staticmethod
    def get_query_string(request):
        return request.META.get('QUERY_STRING')

    @staticmethod
    def get_cookies(request):
        return request.COOKIES

    @staticmethod
    def get_request_headers(request):
        regex = re.compile('^HTTP_')
        a = dict((regex.sub('', header), value) for (header, value)
                 in request.META.items() if header.startswith('HTTP_'))
        return a
