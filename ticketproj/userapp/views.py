import re
from django.shortcuts import redirect, render, get_object_or_404
from userapp.models import * 
from django.contrib import messages

# Create your views here.
def user_login(request):

    if request.method == "POST":
        mobile=request.POST.get('mobile')
        pwd=request.POST.get('pwd')

        try:
            check = UserModel.objects.get(mobile=mobile,pwd=pwd)
            request.session['user_id'] = check.user_id
            return redirect('user-home')
        except Exception:
            return redirect('investor-login')

    return render(request,'user-login.html')



def user_register(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pwd = request.POST.get('pwd')

        if UserModel.objects.filter(mobile=mobile):
            messages.error(request,'Mobile No. Already Exists')
        else:
            UserModel.objects.create(name=name,email=email,mobile=mobile,pwd=pwd)
            messages.success(request,'Registered Successfully!')
            return redirect('user-login')

    return render(request,'user-register.html')



def user_home(request):
    user_id = request.session['user_id']

    obj = get_object_or_404(UserModel,user_id=user_id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subj')
        message = request.POST.get('message')

        obj.name = name
        obj.email = email
        obj.subject = subject
        obj.message = message
        obj.save(update_fields=['name','email','subject','message'])
        obj.save()

    data = UserModel.objects.filter(user_id=user_id)
    print(data)

    return render(request,'user-home.html',{'data':data})



def user_view_status(request):
    user_id = request.session['user_id']

    status = UserModel.objects.filter(user_id=user_id)
    print("-"*50)
    print(status)

    return render(request,'user-view-status.html',{'status':status})