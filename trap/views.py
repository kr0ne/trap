import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from trap.models import ReqRecords, Traps
from request_helper import CurrentRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from trap.forms import CreateNewTrap

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
    pages = Paginator(all_records, 10)
    page = request.GET.get('page')
    try:
        records = pages.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        records = pages.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        records = pages.page(pages.num_pages)
    context = RequestContext(request, {
        'pages': records,
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


@csrf_exempt
def create_new_trap(request):
    context = RequestContext(request)
    # A HTTP POST?
    if request.method == 'POST':
        form = CreateNewTrap(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            # TODO create new view after creating new trap
            return all_requests(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CreateNewTrap()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('add-new-trap.html', {'form': form, 'title': "Create new trap"}, context)
    #
    #
    # print request.POST
    # context = RequestContext(request, {
    #     'title': "Create new trap",
    # })
    # template = loader.get_template('add-new-trap.html')
    # return HttpResponse(template.render(context))


def show_traps_list(request):
    all_traps = Traps.objects.all().order_by('id')
    context = RequestContext(request, {
        'all_traps': all_traps,
    })
    template = loader.get_template('all_traps.html')
    return HttpResponse(template.render(context))
