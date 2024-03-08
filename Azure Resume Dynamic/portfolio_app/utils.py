from .models import *

def counter():
    visitors, created = Site_Visitors.objects.get_or_create(pk=1)    
    return visitors.increment()

def get_projs():
    projects = Projects.objects.all()
    return projects
    