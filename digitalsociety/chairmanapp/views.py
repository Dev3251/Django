from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from random import *
from django.core.mail import send_mail
# Create your views here.
def home(request):
     if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role =="chairman":
            cid=Chairman.objects.get(user_id=uid)
            context ={
                        'uid' : uid,
                        'cid' : cid,
                    }
            return render(request,"chairmanapp/index.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            context ={
                        'uid' : uid,
                        'sid' : sid,
                    }
            return render(request,"societymemberapp/index.html",context)
     else:
       return redirect("login")
        
def login(request):
    if "email" in request.session:
       return redirect("home")
    else:
        if request.POST:
            p_email=request.POST['email']
            p_password=request.POST['password']
            try:
                uid=User.objects.get(email=p_email)
                if uid.password == p_password:
                    if uid.role=="chairman":
                        cid=Chairman.objects.get(user_id=uid)
                        print("------>Sign in button pressed---->",uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email']=uid.email #session store
                        # request.session.set_expiry(10)
                        return redirect("home")
                    else:
                        sid=Societymember.objects.get(user_id=uid)
                        print("------>Sign in button pressed---->",uid)
                        print(uid.role)
                        print(uid.password)
                        request.session['email']=uid.email #session store
                        return redirect("home")
                else:
                    context={
                        'e_msg' : "Invalid Password !!"
                    }
                    print("-------------------Something went wrong")
                    return render(request,"chairmanapp/login.html",context)
            except:
                context={
                        'e_msg' : "Invalid Email Address !!"
                    }
                print("-------------------Something went wrong")
                return render(request,"chairmanapp/login.html",context)
        else:
            print("------>Login page refresh")
            return render(request,"chairmanapp/login.html")
        
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("home")
    else:
        return redirect("home")
    
def chairman_profile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            if request.POST:
                cid.firstname=request.POST['firstname']
                cid.lastname=request.POST['lastname']

                if "picture" in request.FILES:
                    cid.pic=request.FILES['picture']

                cid.save()
                context ={
                                'uid' : uid,
                                'cid' : cid,
                            }
                return render(request,"chairmanapp/profile.html",context)
            else:
                context ={
                                'uid' : uid,
                                'cid' : cid,
                            }
                return render(request,"chairmanapp/profile.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            if request.POST:
                sid.firstname=request.POST['firstname']
                sid.lastname=request.POST['lastname']

                if "picture" in request.FILES:
                    sid.pic=request.FILES['picture']

                sid.save()
                context ={
                                'uid' : uid,
                                'sid' : sid,
                            }
                return render(request,"societymemberapp/profile.html",context)
            else:
                context ={
                                'uid' : uid,
                                'sid' : sid,
                            }
                return render(request,"societymemberapp/profile.html",context)
    else:
        return redirect("login")
    
def chairman_change_password(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            if request.POST:
                current_password=request.POST['c_password']
                new_password=request.POST['n_password']
                if uid.password==current_password:
                    uid.password=new_password
                    uid.save()
                    return redirect("logout")
                else:
                    context={
                        'p_msg' : "Incorrect Password !!"
                    }
                    print("-------------------Something went wrong")
                    return render(request,"chairmanapp/profile.html",context)
            context ={
                            'uid' : uid,
                            'cid' : cid,
                        }
            return render(request,"chairmanapp/profile.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            if request.POST:
                current_password=request.POST['c_password']
                new_password=request.POST['n_password']
                if uid.password==current_password:
                    uid.password=new_password
                    uid.save()
                    return redirect("logout")
                else:
                    context={
                        'p_msg' : "Incorrect Password !!"
                    }
                    print("-------------------Something went wrong")
                    return render(request,"chairmanapp/profile.html",context)
            context ={
                            'uid' : uid,
                            'sid' : sid,
                        }
            return render(request,"societymemberapp/profile.html",context)
    else:
        if uid.role=="chairman":
            context ={
                            'uid' : uid,
                            'cid' : cid,
                        }
            return render(request,"chairmanapp/profile.html",context)
        else:
            context ={
                            'uid' : uid,
                            'sid' : sid,
                        }
            return render(request,"societymemberapp/profile.html",context)
        
def add_member(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            dob=request.POST['contact']
            contact=request.POST['contact']
            city=request.POST['city']
            dob=request.POST['dob']
            num_fam=request.POST['num_fam']
            block=request.POST['block']
            blood=request.POST['blood']
            ownership=request.POST['ownership']
            occupation=request.POST['occupation']
            vehicle_details=request.POST['vehicle_details']

            l1=['d2k','5gg','8oiy','ds4','g5h','8up','lk3f']
            password=email[4:7]+contact[3:6]+choice(l1)

            if "picture" in request.FILES:
                    pic=request.FILES['picture']
                    
                    uid = User.objects.create(email=email,password=password,role="societymember")
                    sid = Societymember.objects.create(user_id=uid,firstname=firstname,lastname=lastname,
                    contact_no=contact,city=city,block_no=block,occupation=occupation,ownership=ownership
                    ,dob=dob,no_of_familymembers=num_fam,blood_group=blood,vehicles_detils=vehicle_details,pic=pic)
            else:        
                uid = User.objects.create(email=email,password=password,role="societymember")
                sid = Societymember.objects.create(user_id=uid,firstname=firstname,lastname=lastname,
                contact_no=contact,city=city,block_no=block,occupation=occupation,ownership=ownership
                ,dob=dob,no_of_familymembers=num_fam,blood_group=blood,vehicles_detils=vehicle_details)

            if sid:
                send_mail("Digital Society Password","Your Password is : "+str(password),"dkdudhia2003@gmail.com",[email])
                msg="Successfully Societymember Created !! Please Check Gmail For Password"
                context={
                    'msg':msg,
                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request,"chairmanapp/add-member.html",context)
        else:
            context ={
                        'uid' : uid,
                        'cid' : cid,
                            }
            return render(request,"chairmanapp/add-member.html",context)
    else:
        return redirect("login")
    
def add_notice(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            nid=Notice.objects.create(
                user_id=uid,
                title=request.POST['title'],
                description=request.POST['description'],
            )
            nall=Notice.objects.all()
            context ={
                        'uid' : uid,
                        'cid' : cid,
                        'nall' : nall,
                            }
            return render(request,"chairmanapp/notice-list.html",context)
        else:
            context ={
                        'uid' : uid,
                        'cid' : cid,
                        # 'nid' : nid,
                            }
            return render(request,"chairmanapp/add-notice.html",context)
    else:
        return redirect("login")
    
def view_notice(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            nall=Notice.objects.all()
            context ={
                            'uid' : uid,
                            'cid' : cid,
                            'nall' : nall,  
                                }
            return render(request,"chairmanapp/notice-list.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            nall=Notice.objects.all()
            context ={
                            'uid' : uid,
                            'sid' : sid,
                            'nall' : nall,  
                                }
            return render(request,"societymemberapp/notice-list.html",context)
    
def view_notice_details(request,pk):
    if "email" in request.session:
        print("------------>pk",pk)
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            notice=Notice.objects.filter(id = pk)
            context ={
                            'uid' : uid,
                            'cid' : cid,
                            'notice' : notice,  
                                }
            return render(request,"chairmanapp/notice-details.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            notice_id=Notice.objects.get(id=pk)
            nall=NoticeViews.objects.filter(user_id=uid,notice_id=notice_id)

            if len(nall)==0:
                nid = NoticeViews.objects.create(user_id=uid,notice_id=notice_id)

            notice=Notice.objects.filter(id = pk)
            context ={
                            'uid' : uid,
                            'sid' : sid,
                            'notice' : notice,  
                                }
            return render(request,"societymemberapp/notice-details.html",context)
        
def all_societymembers(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            sall=Societymember.objects.all()
            context ={
                        'uid' : uid,
                        'cid' : cid,
                        'sall':sall,
                            }
            return render(request,"chairmanapp/all-societymembers.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            call=Chairman.objects.all()
            sall=Societymember.objects.all()
            context ={
                        'uid' : uid,
                        'sid' : sid,
                        'sall':sall,
                        'call':call
                            }
            return render(request,"societymemberapp/all-societymembers.html",context)
        
def specific_societymember_profile(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            sid=Societymember.objects.get(id=pk)
            context ={
                        'uid' : uid,
                        'cid' : cid,
                        'sid':sid,
                            }
            return render(request,"chairmanapp/specific-societymember-profile.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            sd=Societymember.objects.get(id=pk)
            context ={
                        'uid' : uid,
                        'sid' : sid,
                        'sd' : sd,
                            }
            return render(request,"societymemberapp/specific-societymember-profile.html",context)
    
def specific_chairman_profile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            context ={
                        'uid' : uid,
                        'cid' : cid,
                            }
            return render(request,"chairmanapp/specific-chairman-profile.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            call=Chairman.objects.all()
            context ={
                        'uid' : uid,
                        'sid' : sid,
                        'call':call
                            }
            return render(request,"societymemberapp/specific-chairman-profile.html",context)

def add_event(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            eid=Event.objects.create(
                user_id=uid,
                title=request.POST['title'],
                date=request.POST['date'],
                description=request.POST['description'],
            )
            eall=Event.objects.all()
            context ={
                        'uid' : uid,
                        'cid' : cid,
                        'eall' : eall,
                            }
            return render(request,"chairmanapp/event-list.html",context)
        else:
            context ={
                        'uid' : uid,
                        'cid' : cid,
                        # 'nid' : nid,
                            }
            return render(request,"chairmanapp/add-event.html",context)
    else:
        return redirect("login")
    
def view_event(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            eall=Event.objects.all()
            context ={
                            'uid' : uid,
                            'cid' : cid,
                            'eall' : eall,  
                                }
            return render(request,"chairmanapp/event-list.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            eall=Event.objects.all()
            context ={
                            'uid' : uid,
                            'sid' : sid,
                            'eall' : eall,  
                                }
            return render(request,"societymemberapp/event-list.html",context)
      
def view_event_details(request,pk):
    if "email" in request.session:
        print("------------>pk",pk)
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            event=Event.objects.filter(id = pk)
            context ={
                            'uid' : uid,
                            'cid' : cid,
                            'event' : event,  
                                }
            return render(request,"chairmanapp/event-details.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            event_id=Event.objects.get(id=pk)
            eall=EventView.objects.filter(user_id=uid,event_id=event_id)

            if len(eall)==0:
                eid = EventView.objects.create(user_id=uid,event_id=event_id)

            event=Event.objects.filter(id = pk)
            context ={
                            'uid' : uid,
                            'sid' : sid,
                            'event' : event,  
                                }
            return render(request,"societymemberapp/event-details.html",context)

def add_complaint(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        sid=Societymember.objects.get(user_id=uid)
        if request.POST:
            comid=Complaint.objects.create(
                user_id=uid,
                description=request.POST['description'],
            )
            comall=Complaint.objects.all()
            context ={
                        'uid' : uid,
                        'sid' : sid,
                        'comall' : comall,
                            }
            return render(request,"societymemberapp/complaint-list.html",context)
        else:
            context ={
                        'uid' : uid,
                        'sid' : sid,
                        # 'nid' : nid,
                            }
            return render(request,"societymemberapp/add-complaint.html",context)
    else:
        return redirect("login")

def view_complaint(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            comall=Complaint.objects.all()
            context ={
                            'uid' : uid,
                            'cid' : cid,
                            'comall' : comall,  
                                }
            return render(request,"chairmanapp/complaint-list.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            comall=Complaint.objects.all()
            context ={
                            'uid' : uid,
                            'sid' : sid,
                            'comall' : comall,  
                                }
            return render(request,"societymemberapp/complaint-list.html",context)
    
def view_complaint_details(request,pk):
    if "email" in request.session:
        print("------------>pk",pk)
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            complaint_id=Complaint.objects.get(id=pk)
            comall=ComplaintView.objects.filter(user_id=uid,complaint_id=complaint_id)

            if len(comall)==0:
                coid = ComplaintView.objects.create(user_id=uid,complaint_id=complaint_id)

            complaint=Complaint.objects.filter(id = pk)
            context ={
                            'uid' : uid,
                            'cid' : cid,
                            'complaint' : complaint,  
                                }
            return render(request,"chairmanapp/complaint-details.html",context)
        else:
            sid=Societymember.objects.get(user_id=uid)
            complaint=Complaint.objects.filter(id = pk)
            context ={
                            'uid' : uid,
                            'sid' : sid,
                            'complaint' : complaint,
                                }
            return render(request,"societymemberapp/complaint-details.html",context)
                  
def forgot_password(request):
    if request.POST:
        email=request.POST['email']
        otp=randint(1111,9999)

        try:
            uid = User.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail("Forgot Password","Your OTP is : "+str(otp),"dkdudhia2003@gmail.com",[email])
            context={
                "email": email
            }

            return render(request,"chairmanapp/change-password.html",context)
        
        except:
            context={
                "e_msg":"Invalid Email Address !!"
            }
            return render(request,"chairmanapp/forgot-password.html",context)
        
    else:
        return render(request,"chairmanapp/forgot-password.html")
    
def change_password(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        newpassword=request.POST['n_password']
        confirmpassword=request.POST['c_password']

        uid=User.objects.get(email=email)
        if str(uid.otp)==otp:
            if newpassword==confirmpassword:
                uid.password=newpassword
                uid.save()
                context={
                    "msg":"Password Successfully Changed !!"
                }
                return render(request,"chairmanapp/login.html",context)
            else:
                context={
                    "e_msg":"Invalid Password !!"
                }
                return render(request,"chairmanapp/change-password.html",context)
        else:
            context={
                    "e_msg":"Invalid OTP !!"
                }
            return render(request,"chairmanapp/change-password.html",context)
