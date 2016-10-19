from django.http import HttpResponse, QueryDict
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from trap.models import ReqRecords
from request_helper import CurrentRequest


def requests(request):
    all_records = ReqRecords.objects.all().order_by('-id')

    context = RequestContext(request, {
        'all_records': all_records,
    })
    template = loader.get_template('request.html')
    return HttpResponse(template.render(context))
    # test link = http://127.0.0.1:8000/some/page?value=1&format_field=1


@csrf_exempt
def current_request(request):
    current_request = CurrentRequest(request)
    record = ReqRecords(req_date=current_request.req_time, rem_ip=current_request.rem_ip,
                        req_method=current_request.req_method, scheme=current_request.scheme,
                        query_string=current_request.query_string, query_parameters=current_request.query_parameters,
                        cookies=current_request.cookies,
                        headers=current_request.headers)
    record.save()
    context = RequestContext(request, {
        'cur_req': current_request,
    })
    template = loader.get_template('all_requests.html')
    return HttpResponse(template.render(context))
