from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import datetime

def index(request):
    context = {
    }

    return render(request, "engine/index.html", context)
