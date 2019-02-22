from django.shortcuts import render
from django.http import HttpResponse
import datetime
def post_list(request):
    return render(request,'blog/post_list.html',{})
