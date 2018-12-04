from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Applicant, Corporate


def hello(request):
    applicants = Applicant.objects.all()
    template = loader.get_template('name.html')
    context = {
        'applicants': applicants,
    }
    return HttpResponse(template.render(context, request))


def detail(request, applicants):
    return HttpResponse("<h2>applicants: "+str(applicants)+"</h2>")


