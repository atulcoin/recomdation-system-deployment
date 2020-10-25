from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 
import pandas as pd
from sklearn.externals import joblib
reloadmodel = joblib.load('./models/titanicmodel.pkl')

def home(request):
  con1 = homeform(request.POST or None)
  return render(request,'home.html', {'name':'Wellcome to cancer predictions','link':'https://github.com/atulcoin', 'form':con1})

from .forms import homeform
def add(request):
  
  if request.method == 'POST':
    con1 = homeform(request.POST or None)
    if con1.is_valid():
      val1 = con1.cleaned_data['pclass']
      val2 = con1.cleaned_data['pesangerage']
      val3 = con1.cleaned_data['gender']
      name = con1.cleaned_data['name']
      addr = con1.cleaned_data['address']
      sal = con1.cleaned_data['salary']

      res = 'res teriwatt lagg gyi'
      res2 = 'res1 ghar me reh'

      
      formdata={'name':[name],'address':[addr],'salary':[sal]}
      request.session['newformdata']=formdata
  
      new_data ={'Pclass': [val1], 'Age':[val2], 'Sex':[val3]}
      nwdf=pd.DataFrame(new_data, columns =['Pclass','Age', 'Sex'])
      print(nwdf)
      if reloadmodel.predict(nwdf) == 0:
       return render(request,'result.html', {'result':res,'link':'http://127.0.0.1:8000', 'form':con1})
      if reloadmodel.predict(nwdf) == 1:
       return render(request,'result2.html', {'result3':res2,'link':'http://127.0.0.1:8000'})

