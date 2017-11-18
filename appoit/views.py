from random import choice
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from doctors.models import *


# Basic AppoitEngineView
def AppoitEngine(request, doctor_id, time_id, time):
    captcha = ''.join([choice('1234567890') for i in range(4)])
    template = 'appoit/schedule.html'
    doc = Doctor.objects.filter(id=doctor_id)
    extra = ExtraTime.objects.filter(id=time)
    return render_to_response(template, {
        'doctor': doc,
        'id_doc': doctor_id,
        'id_time': time_id,
        'timer': time,
        'code': captcha,
        'ext': extra
    })


@csrf_exempt
# Warning View_[@CSRF-EXEMPT]
def checkAppoit(request):
    if request.POST:
        # Generation secret-code
        secret = ''.join([choice('1234567890') for i in range(4)])
        # REQUEST FROM appoitEngine ...[hidden form]
        doc = request.POST.get('doctor')
        timer = request.POST.get('time')
        time_id = request.POST.get('time_identify')
        # REQUEST FROM appoitEngine.....[user_open_form]
        lastname = request.POST.get('lastname')
        mail = request.POST.get('email')
        phone = request.POST.get('phone')
        # Validate phone and EMAIL
        add = Schedule.objects.create(
            people_name=lastname,
            people_phone=phone,
            people_email=mail,
            secret_code=secret,
            doct=doc,
            data=time_id,
            time=timer,
        ).save()
        template = 'appoit/check_schedule.html'
        return render_to_response(template, {
            'code': secret,
            'id_time': time_id,
            'time': timer,
            'telephone': phone
        })

    else:
        # REQUEST ''''''IS'''''''' NOT POST
        return redirect('/')


@csrf_exempt
def secret(request):
    if request.POST:
        # get Phone_number
        phone = request.POST.get('telephone', '')
        # get time_id models WHERE id = models.time_id for auth
        time_id = request.POST.get('time_id', '')
        secret = request.POST.get('secret')
        timer = request.POST.get('time', '')
        check = Schedule.objects.filter(secret_code=secret)
        if len(check) is not None:
            delt = ExtraTime.objects.filter(id=timer)
            delt.delete()
            alert = 'appoit/complete.html'
            return render_to_response(alert)
        else:
            check.filter(people_phone=phone).delete()
            return redirect('/')
    else:
        return redirect('/')


def doctor_Details(request, doctor_id):
    doc = Doctor.objects.filter(id=doctor_id)
    data = Time.objects.filter(doc_id__id=doctor_id)
    timer = ExtraTime.objects.filter(time_id__doc_id__id=doctor_id)
    template = 'doctor/doctor.html'
    return render_to_response(template,
                              {
                                  'app': doc,
                                  'time': timer,
                                  'extra': data,
                                  'doctor': doc
                              })