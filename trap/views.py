from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def requests(request):
    return HttpResponse("You're on the requests page")

@csrf_exempt
def homepage(request):
    # date = datetime.datetime.today()
    # a = request.get_full_path()
    stringa = ""
    # if request.method == "POST":
    #     c = dict(request.POST.lists())
    #     for k, v in c.items():
    #         stringa += "key=%s, value=%s\t" % (k, v[0])
    #     return HttpResponse(str(date) + "\t" + a + "\t" + stringa)
    # else:
    #     return HttpResponse(str(date) + "\t" + a)
    #test limk = http://127.0.0.1:8000/some/page?value=1&foramat_field=1
    req_array = {}
    req_array['req_time'] = datetime.now()
    req_array['rem_ip'] = request.META.get('REMOTE_ADDR')
    #TODO make rem ip for all caeses. Need add check request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
    req_array['req_method'] = request.method
    req_array['scheme'] = request.scheme
    req_array['query_string'] = request.META.get('QUERY_STRING')
    a = dict(request.GET.lists())
    for k, v in a.items():
        stringa += "key=%s, value=%s\t" % (k, v[0])
    req_array['query_parameters'] = stringa
    req_array['cookies'] = request.COOKIES
    req_array['headers'] = request.META
    context = RequestContext(request, {
        'req_array': req_array,
    })
    template = loader.get_template('requests.html')
    return HttpResponse(template.render(context))
