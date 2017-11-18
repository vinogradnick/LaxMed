from django.shortcuts import render, render_to_response


# Create your views here.
def index(request):
    template = 'doctor/doctor_profile.html'
    return render_to_response(template)