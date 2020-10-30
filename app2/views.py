from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import emp
from .models import movieId
import pandas as pd
from .models import Ratings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import json


# Create your views here.
def recomdation(request):
    data1 = movieId.objects.all()
    return render(request,"result2.html",{'data1':data1})

def logout(request):
    auth.logout(request)
    return redirect('/')

def vidb(request):
    data = movieId.objects.all()
    return render(request,"vdb.html",{'data':data})
    

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else :
            messages.info(request,'Sorry Wrong Password')
            return redirect("login")
    else:
        return render(request,'login.html')



def singup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already exists')
                return redirect('singup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('singup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user Created')
                return redirect('singup')
        else:
            messages.info(request,'password missmatch')
            return redirect('singup')

    else:
        return render(request,'sing.html')

from .forms import inputdata
def form1(request):
    con = inputdata(request.POST or None)
    savedata=request.session.get('newformdata')
    print(savedata)
    if request.method == 'POST':
        
        if con.is_valid():
            n98 = con.cleaned_data['first_name']
            data1 = con.cleaned_data['addresss']
            s981 = con.cleaned_data['salary']
            status=con.cleaned_data['status']
            emp(Name=n98,address=data1,salary=s981,status=status).save()
            msg="Data Stored Successfully"
            return render(request,"form1.html",{'msg':msg,'form':con})
    return render(request,'form1.html',{'form':con})

def delete(request):
    nisha = request.GET['id']
    emp.objects.filter(id=nisha).delete()
    return redirect('vidb')




def monkey(request):
    if request.method == 'POST':
        if request.POST.get('title'):
            n98 = movieId()
            n98=request.POST.get('title')
            #print(n98)
            movies=pd.DataFrame(list(movieId.objects.all().values('movieId','title','genres')))
            ratings=pd.DataFrame(list(Ratings.objects.all().values('userId','movieId','rating')))
            #print(df.head())
            movies['genres']= movies['genres'].str.replace('|',' ')
            ratings_f = ratings.groupby('userId').filter(lambda x: len(x) >=100)
            movie_list_rating =ratings_f.movieId.unique().tolist()
            movies = movies[movies.movieId.isin(movie_list_rating)]
            tfidfvec = TfidfVectorizer(stop_words='english') 
            tfidf_movieid = tfidfvec.fit_transform((movies["genres"]))
            tf_df=pd.DataFrame(tfidf_movieid.toarray(), index=movies.index.tolist())
            pca = PCA(n_components=12)
            matrix = pca.fit_transform(tf_df)
            ratings_f1=pd.merge(movies[['movieId']], ratings_f, on="movieId", how="right")
            ratings_f2=ratings_f1.pivot(index='movieId', columns='userId', values = 'rating').fillna(0)
            pca1 = PCA(n_components=30)
            matrix2 = pca1.fit_transform(ratings_f2)
            matrix1_df=pd.DataFrame(matrix[:,0:12], index=movies.title.tolist())
            matrix2_df=pd.DataFrame(matrix2,index=movies.title.tolist())
            a_1 = np.array(matrix1_df.loc[n98]).reshape(1,-1)
            a_2 = np.array(matrix2_df.loc[n98]).reshape(1,-1)
            score1=cosine_similarity(matrix1_df,a_1).reshape(-1)
            score2=cosine_similarity(matrix2_df,a_2).reshape(-1)
            hybrid = ((score1 + score2)/2.0)
            dictdf= {'content':score1, 'collibrative':score2, 'hybrid':hybrid}
            similar= pd.DataFrame(dictdf, index= matrix1_df.index)
            similar.sort_values('hybrid', ascending=False, inplace=True)
            output=similar[1:].head(10)
            json_record = output.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_record)
            context={'d':data}




            return render(request,"result.html",context)


