import re
from datetime import datetime
from django.utils import timezone


def get_current_time():
    current_time = timezone.now()
    return current_time


def get_rem_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_request_method(request):
    return request.method


def get_request_scheme(request):
    return request.scheme


def get_query_string(request):
    return request.META.get('QUERY_STRING')


def get_query_parameters(request):
    method = get_request_method(request)
    pretty_string = ""
    if method == 'GET':
        pretty_string += "\nGet parameters: \n"
        get_dict = request.GET
        return get_dict
        #for k, v in get_dict.items():
        #    pretty_string += "key=%s, value=%s\n" % (k, v)
    elif method == 'POST':
        post_dict = request.POST
        if post_dict:
            pretty_string += "Post parameters: "
            for k, v in post_dict.items():
                pretty_string += "key=%s, value=%s\t" % (k, v)
        get_dict = request.GET
        if get_dict:
            get_string = "\nGet parameters:\n"
            for j,h in get_dict.items():
                get_string += "key=%s, value=%s\t" % (j, h[0])
        pretty_string = pretty_string + get_string
    return pretty_string


def get_cookies(request):
    return request.COOKIES


def get_request_headers(request):
    regex = re.compile('^HTTP_')
    a = dict((regex.sub('', header), value) for (header, value)
        in request.META.items() if header.startswith('HTTP_'))
    return a