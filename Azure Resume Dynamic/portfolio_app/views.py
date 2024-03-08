from django.shortcuts import render
from .utils import *
# Create your views here.

def index(req):
    return render(req,"index.html",{"counter":counter(),"projects":get_projs()})