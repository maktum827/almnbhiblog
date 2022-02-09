from django.shortcuts import render
from .models import Admission, Banner, Course

# Create your views here.
def home(request):
    bnrs = Banner.objects.all()
    courses = Course.objects.all()

    params = {
        'banners': bnrs,
        'courses': courses,
    }
    return render(request, 'index.html', params)

def courses(request):
    return render(request, 'courses.html')

def admission(request):
    if request.method =="POST":
         name = request.POST.get('name','')
         address = request.POST.get('address', '')
         phone = request.POST.get('mobile','')
         email = request.POST.get('email','')
         scrnsht = request.FILES.get('scrnsht','')
         student = Admission(name = name,address = address ,mobile = phone, email = email,image=scrnsht)
         student.save()

    return render(request, 'admission.html')

def about(request):
    return render(request, 'about.html')