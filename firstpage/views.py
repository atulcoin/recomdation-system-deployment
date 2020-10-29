from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 
import pandas as pd
from sklearn.externals import joblib
reloadmodel = joblib.load('./models/titanicmodel.pkl')

def home(request):
  con1 = homeform(request.POST or None)
  return render(request,'home.html', {'name':'Wellcome to Hybrid movie prediction','link':'https://github.com/atulcoin', 'form':con1})

from .forms import homeform
def add(request):
  pass