from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import *

# Create your views here.
def admin_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        if username == 'admin' and pwd == 'admin':
            return redirect('admin-view-ticket')
    return render(request,'admin-login.html')


def admin_view_ticket(request):

    ticket = UserModel.objects.all()
    return render(request,'admin-view-ticket.html',{'ticket':ticket})


def accept(request,id):
    accept = get_object_or_404(UserModel, user_id = id)
    accept.status = "Accepted"
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin-view-ticket')


def reject(request,id):
    reject = get_object_or_404(UserModel, user_id=id)
    reject.status = "Rejected"
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('admin-view-ticket')