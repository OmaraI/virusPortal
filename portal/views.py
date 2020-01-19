from django.shortcuts import render, render_to_response
from django.db.models import Count
import pandas as pd
import numpy as np
from portal.models import *
from portal.forms import *

def  home(request):  
  outbreak = pd.DataFrame(list(outbreaks.objects.all().values()))
  return render(request, 'index.html',
              {'outbreak': outbreak})
  
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

def search(request):

   outbreak=outbreaks.objects.all()  
  
   return render(request, 'search.html',{
          'outbreak':outbreak,
   })

def summary(request):
  outbreak = pd.DataFrame(list(outbreaks.objects.all().values()))
  context={'outbreak':'outbreak'}
  return render(request, 'summary.html', context=context)

def etax(request):
    e_tax = pd.read_csv("/Users/macbook/Desktop/e_tax_data.csv")
    #obtain data for different measures of performance
    correctness=e_tax[e_tax.major=='correctness'].groupby('minor', as_index=False)['participants'].sum() 
    L=[]
    for index, row in correctness.iterrows(): 
      desp=row['minor'] 
      count=row['participants'] 
      tmp=[desp, count] 
      #print(tmp) 
      L.append(tmp) 
    
    availability=e_tax[e_tax.major=='availability'].groupby('minor', as_index=False)['participants'].sum() 
    avail_list=[]
    for index, row in availability.iterrows(): 
      desp=row['minor'] 
      count=row['participants'] 
      tmp=[desp, count] 
      #print(tmp) 
      avail_list.append(tmp)

    error_data=e_tax[e_tax.major=='maturity'].groupby('minor', as_index=False)['participants'].sum() 
    error_list=[]
    for index, row in error_data.iterrows(): 
      desp=row['minor'] 
      count=row['participants'] 
      tmp=[desp, count] 
      #print(tmp) 
      error_list.append(tmp)

    age=e_tax[e_tax.major=='age'].groupby('minor', as_index=False)['participants'].sum() 
    age_list=[]
    for index, row in age.iterrows(): 
      desp=row['minor'] 
      count=row['participants'] 
      tmp=[desp, count] 
      #print(tmp) 
      age_list.append(tmp)

    gender=e_tax[e_tax.major=='gender'].groupby('minor', as_index=False)['participants'].sum() 
    gender_list=[]
    for index, row in gender.iterrows(): 
      desp=row['minor'] 
      count=row['participants'] 
      tmp=[desp, count] 
      #print(tmp) 
      gender_list.append(tmp)

    interface=e_tax[e_tax.major=='learnability'].groupby('minor', as_index=False)['participants'].sum() 
    interface_list=[]
    for index, row in interface.iterrows(): 
      desp=row['minor'] 
      count=row['participants'] 
      tmp=[desp, count] 
      #print(tmp) 
      interface_list.append(tmp)
    
    context={
    'correctness': L, 
    'availability': avail_list,
    'error_data': error_list,
    'age_list': age_list,
    'gender': gender_list,
    'interface': interface_list
    } ;
    
    return render(request, 'etax.html', context=context)