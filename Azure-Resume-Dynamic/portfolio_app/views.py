from django.shortcuts import render
from .utils import *
# Create your views here.

def index(req):
    context = {
        "counter":counter(),
        "projects":get_projs(),
        "certifications":get_certs(),
        "work": get_work()
    }
    return render(req,"index.html",context)