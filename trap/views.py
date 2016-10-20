from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from trap.models import ReqRecords
from request_helper import CurrentRequest

# test link = http://127.0.0.1:8000/some/page?value=1&format_field=1


def all_requests(request):
    all_records = ReqRecords.objects.all().order_by('-id')
    for record in all_records:
        if record.query_parameters:
            temp = eval(record.query_parameters)
            record.query_parameters = temp
        if record.cookies:
            temp = eval(record.cookies)
            record.cookies = temp
        if record.headers:
            temp = eval(record.headers)
            record.headers = temp
    context = RequestContext(request, {
        'all_records': all_records,
    })
    template = loader.get_template('all_requests.html')
    return HttpResponse(template.render(context))


@csrf_exempt
def current_request(request):
    current_request_data = CurrentRequest(request)
    record = ReqRecords(req_date=current_request_data.req_time,
                        rem_ip=current_request_data.rem_ip,
                        req_method=current_request_data.req_method,
                        scheme=current_request_data.scheme,
                        query_string=current_request_data.query_string,
                        query_parameters=current_request_data.query_parameters,
                        cookies=current_request_data.cookies,
                        headers=current_request_data.headers)
    record.save()
    context = RequestContext(request, {
        'cur_req': current_request_data,
    })
    template = loader.get_template('current_request.html')
    return HttpResponse(template.render(context))
