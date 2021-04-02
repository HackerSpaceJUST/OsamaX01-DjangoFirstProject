import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'birthday/index.html', {
        "flag": now.day == 31 and now.month == 12
    })
