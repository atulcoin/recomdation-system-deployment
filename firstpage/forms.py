from django import forms


gender = [(1,'male'),(0,'female')]
class homeform(forms.Form):
    name=forms.CharField(max_length=200)
    address = forms.CharField( max_length = 200)
    salary=forms.IntegerField(help_text='enter the salary')
    pclass=forms.IntegerField(max_value=1)
    pesangerage=forms.IntegerField()
    gender=forms.CharField(widget=forms.Select(choices=gender))