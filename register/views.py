from atexit import register
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User

def user_list(request):
    context={'user_list':User.objects.all()}
    return render(request, "register/user_list.html",context)

def user_form(request,id=0): 
    if request.method=="GET":
        if id==0:
            form=UserForm()
        else:
            user=User.objects.get(pk=id)
            form=UserForm(instance=user)
        return render(request, "register/user_form.html",{'form':form})
    else:
        if id==0:
            form=UserForm(request.POST)
        else:
            user=User.objects.get(pk=id)
            form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/register/list')

def user_delete(request,id):
     user=User.objects.get(pk=id)
     user.delete()
     return redirect('/register/list')

