from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def requests(request):
    return HttpResponse("You're on the requests page")

@csrf_exempt
def homepage(request):
    # date = datetime.datetime.today()
    # a = request.get_full_path()
    # stringa = ""
    # if request.method == "POST":
    #     c = dict(request.POST.lists())
    #     for k, v in c.items():
    #         stringa += "key=%s, value=%s\t" % (k, v[0])
    #     return HttpResponse(str(date) + "\t" + a + "\t" + stringa)
    # else:
    #     return HttpResponse(str(date) + "\t" + a)
    req_array = "asdasda"
    context = RequestContext(request, {
        'req_array': req_array,
    })
    template = loader.get_template('requests.html')
    return HttpResponse(template.render(context))
