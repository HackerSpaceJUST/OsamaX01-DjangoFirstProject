from django.shortcuts import render, redirect
from django import forms
import datetime

class DateForm(forms.Form):
    day = forms.IntegerField(label = "Day", min_value = 1, max_value = 31)
    month = forms.IntegerField(label = "Month", min_value = 1, max_value = 12)

def index(request):
    if(request.method == 'POST'):
        form = DateForm(request.POST)
        if(not form.is_valid()):
            return render(request, 'birthdaychecker/index.html', {
                "form" : form
            })
            
        else:
            day = form.cleaned_data['day']
            month = form.cleaned_data['month']
            request.session['day'] = day
            request.session['month'] = month
            return redirect('birthdaychecker:result')

    return render(request, 'birthdaychecker/index.html', {
        "form" : DateForm()
    })

def result(request):
    if 'day' not in request.session:
        return redirect('birthdaychecker:index')
        
    now = datetime.datetime.now()
    return render(request, 'birthdaychecker/result.html', {
        'flag' : request.session['day'] == now.day and request.session['month'] == now.month 
    })
