from .models import *

def counter():
    visitors, created = Site_Visitors.objects.get_or_create(pk=1)    
    return visitors.increment()

def get_projs():
    projects = Project.objects.all()
    return projects

def get_certs():
    certifications = Certification.objects.all()
    return certifications

def get_work():
    work =  Work.objects.all()
    return work   