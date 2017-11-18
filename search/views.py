from django.shortcuts import render, render_to_response, redirect
from doctors.models import *


def index(request):
    template = 'search/search.html'
    return render_to_response(template)


# Search views system
def SearchEngine(request):
    template = 'search/result.html'
    if request.GET:
        q = request.GET['q']
        loc = request.GET['loc']
        appoit = Doctor.objects.filter(specialization=q, location=loc)
        data = Time.objects.filter(doc_id__specialization=q, doc_id__location=loc)
        timer = ExtraTime.objects.filter(time_id__doc_id__specialization=q, time_id__doc_id__location=loc)
        return render_to_response(template,
                                  {
                                      'spec': q,
                                      'location': loc,
                                      'app': appoit,
                                      'time': timer,
                                      'extra': data,
                                  }
                                  )
    else:
        return redirect('/')


def diagnostic_index(request):
    template = 'diagnostic/diagnostic.html'
    return render_to_response(template)
