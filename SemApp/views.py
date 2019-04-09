from django.shortcuts import render
from django.http import HttpResponse
from SemApp.forms import SemMarksForm
from django.core.mail import send_mail
from SemApp import settings
# Create your views here.
def hello(response):
      return HttpResponse("Semester Marks of the Students")

def getSemMarks(request):
      if request.method == 'POST':
          form=SemMarksForm(request.POST)
          if form.is_valid():
              form.save()
      form=SemMarksForm()
      return render(request,"SemMarks.html",{'form':form})

def Mail(request):
     send_mail('python','for check','gokul.prasath88@gmail.com',['gokul.prasath88@gmail.com'])
    