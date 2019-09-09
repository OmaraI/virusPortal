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

def  summary(request):
	return render(request, 'summary.html')

def  guidelines(request):
	return render(request, 'guidelines.html')

def  contact(request):
	return render(request, 'contact.html')
