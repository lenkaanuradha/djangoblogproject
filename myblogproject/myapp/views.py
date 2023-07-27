from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from .forms import Sign_upform,loginform,addform,Postform
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
def homepage(request):
   
    post=Post.objects.all()
    return render(request,'home.html',{'post':post})
def aboutpage(request):
    return render(request,'about.html')
def contactpage(request):
    return render(request,'contact.html')
def user_login(request):
 if not request.user.is_authenticated:
    if request.method == "POST":
     fm=loginform(request=request,data=request.POST)
     if (fm.is_valid()):
       uname=fm.cleaned_data['username']
       upass=fm.cleaned_data['password']
       user=authenticate(username=uname,password=upass)
    
       if user is not None:
        login(request,user)
        messages.success(request,'loggedin  successfully ')
       
        return HttpResponseRedirect('/dashboard/')
     
    else:
     fm=loginform()
    return render(request,'login.html',{'form':fm})
 else:
   return HttpResponseRedirect('/dashboard/')
  
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def user_signup(request):
   if request.method=="POST":
    fm=Sign_upform(request.POST)
    if (fm.is_valid()):
       messages.success(request,'Congratulations!! You have become an author')
       user=fm.save()
       group=Group.objects.get(name="Author")
       user.groups.add(group)
   else:
    fm=Sign_upform()
   return render(request,'signup.html',{'form':fm})
def dashboard(request):
    if request.user.is_authenticated:
      posts=Post.objects.all()
      user=request.user
      fname=user.get_full_name()
      grps=user.groups.all()
      return render(request,'dashboard.html',{'posts':posts,'username':fname,'u':user,'grp':grps})
    else:
      return HttpResponseRedirect("/login/")
 
def add_posts(request):
   if request.user.is_authenticated:
     if request.method == "POST":
       
       post=addform(request.POST)
       if post.is_valid():
        
        post.save()
        post=addform()
     else:
       post=addform()

     return render(request,'addpost.html',{'posts':post})
    
   else:
     return HttpResponseRedirect('/login/')
   
def deletepost(request,id):
 if request.user.is_authenticated:
  if request.method=="POST":
   
    pi=Post.objects.get(pk=id)
    
    pi.delete()
    return HttpResponseRedirect('/dashboard/')
 else:
   return HttpResponseRedirect('/login/')
 
def update(request,id):
  if request.user.is_authenticated:
    if request.method == "POST":

      pi=Post.objects.get(pk=id)
      fm=Postform(request.POST,instance=pi)
      if fm.is_valid():
       
       fm.save()
       fm=Postform()
    else:
      fm=Postform()
    return render(request,'updateform.html',{'posts':fm})

  else:
    return HttpResponseRedirect('/login/')