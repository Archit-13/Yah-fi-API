from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import *
from django.template import RequestContext
from .webscraping import createCSV

# Create your views here.
from django.http import HttpResponse
from .forms import personalForm


def home(request):
     form = personalForm(request.POST or None)
     if form.is_valid():
          picked = form.cleaned_data.get('StockName')
          createCSV(picked)
          f= open("Historicaldata.csv","r")
          lines = f.readlines()
          linesstr = "\n<br/>".join(lines)
          return HttpResponse(linesstr)
     else:
          form = personalForm

     return render(request,'form_template.html', {'form':form })


  