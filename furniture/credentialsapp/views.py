from django.contrib import messages,auth
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
def login(request):
     return render(request,'login.html')
     if request.method=='POST':
          user_name=request.POST['username']
          pass_word=request.POST['password']
          user=auth.authenticate(username=user_name,password=pass_word)

     if user is not None:
              auth.login(request,user)
              return redirect('/')

     else:
          messages.info(request,'invalid credentials')
          return redirect('login')

def register(request):
     if request.method=='POST':
          user_name=request.POST['username']
          first_name=request.POST['firstname']
          last_name=request.POST['lastname']
          e_mail=request.POST['email']
          pass_word=request.POST['password']
          pass_word2=request.POST['password2']
          if pass_word==pass_word2:
               if User.objects.filter(username=user_name).exists():
                    messages.info(request,'Username already taken')
                    return redirect('register')
               elif User.objects.filter(email=e_mail).exists():
                    messages.info(request,"Email already taken")
                    return redirect('register')
               else:
                    user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=e_mail,password=pass_word)
                    user.save();
                    return redirect('login')
          else:
               messages.info(request,'Password not matching')
               return redirect('register')
          return redirect('/')
     return render(request,'register.html')
    # if request.method=='POST':
    #       user_name=request.POST['username']
    #       first_name=request.POST['firstname']
    #       last_name=request.POST['lastname']
    #       e_mail=request.POST['email']
    #       pass_word=request.POST['password']
    #       pass_word2=request.POST['password2']
    #       if pass_word==pass_word2:
    #            if User.objects.filter(username=user_name).exists():
    #                 messages.info(request,'Username already taken')
    #                 return redirect('register')
    #            elif User.objects.filter(email=e_mail).exists():
    #                 messages.info(request,"Email already taken")
    #                 return redirect('register')
    #            else:
    #                 user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=e_mail,password=pass_word)
    #                 user.save();
    #                 return redirect('login')
    #       else:
    #            messages.info(request,'Password not matching')
    #            return redirect('register')
    #       return redirect('/')
    #       return render(request,'register.html')

def logout(request):
     auth.logout(request)
     return redirect('/')
# def register(request):
#      return render(request,'register.html')