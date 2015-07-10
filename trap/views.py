from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.template import RequestContext, loader
from helpers import *
from django.views.decorators.csrf import csrf_exempt
from trap.models import req_records
# Create your views here.

def requests(request):
    return HttpResponse("You're on the requests page")

@csrf_exempt
def homepage(request):

    #test limk = http://127.0.0.1:8000/some/page?value=1&foramat_field=1
    req_array = dict()
    req_array['req_time'] = get_current_time()
    req_array['rem_ip'] = get_rem_ip_address(request)
    req_array['req_method'] = get_request_method(request)
    req_array['scheme'] = get_request_scheme(request)
    req_array['query_string'] = get_query_string(request)
    req_array['query_parameters'] = get_query_parameters(request)
    req_array['cookies'] = get_cookies(request)
    req_array['headers'] = get_request_headers(request)

    record = req_records(req_date=req_array['req_time'], rem_ip=req_array['rem_ip'],
                         req_method=req_array['req_method'], scheme=req_array['scheme'],
                         query_string=req_array['query_string'], query_parameters=req_array['query_parameters'],
                         cookies=req_array['cookies'],
                         headers=req_array['headers'])
    record.save()
    context = RequestContext(request, {
        'req_array': req_array,
    })
    template = loader.get_template('requests.html')
    return HttpResponse(template.render(context))
