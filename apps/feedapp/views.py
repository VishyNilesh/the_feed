from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.

def feedapp(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        data = {
            "all_msgs":Message.objects.all().order_by("-created_at")
        }
        return render(request,"feedapp/feedapp.html",data)
    
def post_message(request):
    thisUser = User.objects.get(id = request.session['user_id'])
    Message.objects.create(user = thisUser, message = request.POST['msgText'])
    return redirect("/feedapp")

def post_comment(request,msg_id):
    thisUser = User.objects.get(id=request.session['user_id'])
    thisMsg = Message.objects.get(id=msg_id)
    Comment.objects.create(message=thisMsg, user=thisUser, comment=request.POST['cmntText'])
    return redirect("/feedapp")

def delete_msg(request,msg_id):
    thisMsg = Message.objects.get(id = msg_id)
    theseComments = thisMsg.comments.all()
    for cmnt in theseComments:
        cmnt.delete()
    thisMsg.delete()
    return redirect("/feedapp")

def user_posts(request,user_id):
    thisUser = User.objects.get(id = user_id)
    data = {
        "user_messages":thisUser.messages.all(),
        "user_comments":thisUser.comments.all()
    }
    return render(request, "feedapp/posts.html",data)

def liked_messages(request,msg_id):
    thisUser = User.objects.get(id = request.session['user_id'])
    thisMsg = Message.objects.get(id = msg_id)
    thisMsg.like.add(thisUser)
    thisMsg.save()
    return redirect("/feedapp")

def liked_comments(request,cmnt_id):
    thisUser = User.objects.get(id = request.session['user_id'])
    thisCmnt = Comment.objects.get(id = cmnt_id)
    thisCmnt.like.add(thisUser)
    thisCmnt.save()
    return redirect("/feedapp")

def logout(request):
    request.session.clear()
    return redirect("/")