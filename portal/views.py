from django.shortcuts import render, render_to_response
from django.db.models import Count
#import pandas as pd
#import numpy as np
from portal.models import *

def  home(request):
	return render(request, 'index.html')

def  search(request):
	return render(request, 'search.html')

def  publications(request):
	return render(request, 'publications.html')

def  guidelines(request):
	return render(request, 'guidelines.html')

def  contact(request):
	return render(request, 'contact.html')

def  downloads(request):
    samples=sample.objects.all()
    viruses=virus.objects.all()
    sites=site.objects.all()
    projects=project.objects.all()
    organisms=organism.objects.all()
    return render(request, 'downloads.html', 
							{'samples': samples, 
              'viruses': viruses,
              'sites': sites,
              'projects': projects,
              'organisms':organisms})

def summary(request):
    samples=sample.objects.all()
    viruses=virus.objects.all()
    sites=site.objects.all()
    projects=project.objects.all()
    organisms=organism.objects.all()

    context={}
    """ context={'xdata_assay': xdata_assay, 
		'ydata_assay': ydata_assay,
		'xdata_disease': xdata_disease, 
		'ydata_disease': ydata_disease, 
		'platform_pie_dict': platform_pie_dict, 
		'site_pie_dict': site_pie_dict, 
		'all_records': all_records};
    """    
    return render(request, 'summary.html', context=context)