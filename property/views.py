from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView,DetailView
from .forms import ContactForm
from django.contrib import messages
from .models import Contact,Products,Newsletter,Work
from datetime import datetime
from django.http import HttpResponse

# Create your views here.

def home(request):

    

    return render(request,"property/index.html")


def contact(request):

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display/about.html")
    else:
        form = ContactForm()
    context = {"form":form}


    return render(request, "property/contact.html",context)

def services(request):
    work=Work.objects.all()
    context={"work":work}

    return render(request,"property/services.html",context)

def service_detail(request):


    return render(request,"property/service1.html")
def about(request):

    return render(request,"property/about.html")

def product(request):
    product=Products.objects.all()
    date=datetime.now()
    context={"product":product,"date":date}

    return render(request,"property/product.html",context)

def send_message(request):
    name =  request.POST['name']
    email =  request.POST['email']
    try:
        subject=request.POST['subject']
    except:
        print("Subject not added!!!!!")
    message =  request.POST['message']

    try:
        message=Contact(name=name,email=email,subject=subject,message=message)
    except:
        message=Contact(name=name,email=email,message=message)
    message.save()

    return HttpResponseRedirect('/contact/')


def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']  # Use get() to handle missing 'email' key

        if email:
            message = Newsletter(email=email)
            message.save()
            return render(request,"property/services.html")
        else:
            return HttpResponse("Invalid email.")
    else:
        return HttpResponse("Invalid request method.")
    
def work_detail(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    pictures = work.pictures_set.all()  # Assuming "pictures" is the related name of the foreign key field in the Pictures model

    context = {
        'work': work,
        'pictures': pictures
    }

    return render(request, 'property/workdetails.html', context)
    

