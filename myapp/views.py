import random

import datetime

import re
import smtplib

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'login_index.html')
def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var1=Login.objects.get(username=username,password=password)
        request.session['lin']='in'
        request.session['lid']=var1.id
        if var1.type=="admin":
            return HttpResponse('''<script>alert('Login Successfull');window.location="/myapp/admin_home/"</script>''')
        elif var1.type=="Depo Officer":
            return HttpResponse('''<script>alert('Login Successfull');window.location="/myapp/depo_officer_home/"</script>''')
        elif var1.type=="user":
            return HttpResponse('''<script>alert('Login Successfull');window.location="/myapp/user_home/"</script>''')
        else:
            return HttpResponse('''<script>alert('User Not Found!!');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid!!');window.location="/myapp/login/"</script>''')


def add_charge(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Admin/Admin Add Charge.html')
def add_charge_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_Place=request.POST['textfield']
    To_Place=request.POST['textfield2']
    Type=request.POST['select']
    Amount=request.POST['textfield3']
    acobj=Charge()
    acobj.From_Place=From_Place
    acobj.To_Place=To_Place
    acobj.Type=Type
    acobj.Amouont=Amount
    acobj.save()
    return HttpResponse('''<script>alert('Charges Addded Succesfully');window.location="/myapp/charge_add/"</script>''')


def edit_charge(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    ob=Charge.objects.get(id=id)
    request.session['cidd']=id
    return render(request,'Admin/Admin edit add charge.html',{'val':ob})
def edit_charge_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_Place=request.POST['textfield']
    To_Place=request.POST['textfield2']
    Type=request.POST['select']
    Amount=request.POST['textfield3']
    acobj = Charge.objects.get(id=request.session['cidd'])
    acobj.From_Place = From_Place
    acobj.To_Place = To_Place
    acobj.Type = Type
    acobj.Amouont = Amount
    acobj.save()
    return HttpResponse('''<script>alert('Edited Succesfull');window.location="/myapp/charge_view/"</script>''')

def delete(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    ob=Charge.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Deleted Succesfully');window.location="/myapp/charge_view/"</script>''')
def view_charges(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    cobj=Charge.objects.all()
    return render(request,'Admin/Admin View charges.html',{"data":cobj})
def view_charges_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search = request.POST['textfield']
    cobj=Charge.objects.filter(From_Place__contains=Search)
    return render(request,'Admin/Admin View charges.html',{"data":cobj})

def add_depo_officer(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Admin/Admin Add Depo Officer.html')
def add_depo_officer_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Name = request.POST['textfield']
    Gender = request.POST['RadioGroup1']
    Date_Of_Birth = request.POST['textfield2']
    Email = request.POST['textfield4']
    if Login.objects.filter(username__icontains=Email).exists():
        return HttpResponse('''<Script>alert("Email all ready Exists");history.back()</Script>''')
    Phone_Number = request.POST['textfield5']
    Depo = request.POST['textfield6']
    Proof = request.FILES['fileField']

    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs = FileSystemStorage()
    fs.save(date, Proof)
    path = fs.url(date)

    lobj = Login()
    lobj.username = Email
    lobj.password =Phone_Number
    lobj.type = "Depo Officer"
    lobj.save()

    adobj=Depo_officer()
    adobj.Name=Name
    adobj.Gender=Gender
    adobj.Date_of_birth=Date_Of_Birth
    adobj.Email=Email
    adobj.Phone_Number=Phone_Number
    adobj.Depo=Depo
    adobj.Proof=path
    adobj.LOGIN=lobj
    adobj.save()
    return HttpResponse('''<script>alert('Addded Succesfully');window.location="/myapp/add_officers/"</script>''')

def view_officers_verify(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dobj = Depo_officer.objects.all()
    return render(request,'Admin/Adim view depo officer and verify.html',{"data":dobj})

def view_officers_verify_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search = request.POST['textfield']
    dobj=Depo_officer.objects.filter(Name__icontains=Search)
    return render(request,'Admin/Adim view depo officer and verify.html',{"data":dobj})

def Edit_DepoOfficers(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    eo=Depo_officer.objects.get(id=id)
    request.session['eoid']=id
    return render(request,'Admin/Admin edit depo officer.html',{'val':eo})

def edit_officers_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Name = request.POST['textfield']
    Gender = request.POST['RadioGroup1']
    Date_Of_Birth = request.POST['textfield2']
    Email = request.POST['textfield4']
    Phone_Number = request.POST['textfield5']
    Depo = request.POST['textfield6']
    if 'fileField' in request.FILES:
        Proof = request.FILES['fileField']

        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, Proof)
        path = fs.url(date)

        adobj=Depo_officer.objects.get(id=request.session['eoid'])
        adobj.Name=Name
        adobj.Gender=Gender
        adobj.Date_of_birth=Date_Of_Birth
        adobj.Email=Email
        adobj.Phone_Number=Phone_Number
        adobj.Depo=Depo
        adobj.Proof=path
        adobj.save()
        return HttpResponse('''<script>alert('Edited Succesfully');window.location="/myapp/View_DepoOfficers/"</script>''')

    else:
        adobj = Depo_officer.objects.get(id=request.session['eoid'])
        adobj.Name = Name
        adobj.Gender = Gender
        adobj.Date_of_birth = Date_Of_Birth
        adobj.Email = Email
        adobj.Phone_Number = Phone_Number
        adobj.Depo = Depo

        adobj.save()
        return HttpResponse(
            '''<script>alert('Edited Succesfully');window.location="/myapp/View_DepoOfficers/"</script>''')


def delete_officers(request, id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dob = Depo_officer.objects.get(id=id)
    dob.delete()
    return HttpResponse('''<script>alert('Deleted Succesfully');window.location="/myapp/View_DepoOfficers/"</script>''')


def view_users(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Users.objects.all()
    return render(request,'Admin/Admin view user.html',{'data':res})
def view_users_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search = request.POST['textfield']
    sus=Users.objects.filter(Name__contains = Search)
    return render(request,'Admin/Admin view user.html',{"data":sus})


def view_complaints(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    com=Complaint.objects.all()
    return render(request,'Admin/Admin view complaints and reply.html',{"data":com})
def view_complaints_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_date=request.POST['textfield']
    To_Date=request.POST['textfield2']
    sd=Complaint.objects.filter(Date__range=[From_date,To_Date])
    return render(request,'Admin/Admin view complaints and reply.html',{'data':sd})

def send_reply(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Admin/Admin reply complaint.html',{'id':id})

def send_reply_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Reply=request.POST['textarea']
    id=request.POST['id']
    resu=Complaint.objects.filter(id=id).update(reply=Reply,status="Replied")
    return HttpResponse('''<script>alert('Success');window.location="/myapp/view_complaint/"</script>''')

def Change_pass_admin(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Admin/Admin Change Password.html')

def Change_pass_admin_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    oldpass=request.POST['textfield']
    newpass=request.POST['textfield2']
    confpass=request.POST['textfield3']
    # return HttpResponse('ok')
    res = Login.objects.filter(id=request.session['lid'], password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = Login.objects.filter(id=request.session['lid'], password=oldpass).update(password=newpass)
            return HttpResponse('''<Script>alert("Password Updated");window.location="/myapp/login/";</Script>''')
        else:
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/myapp/Change_pass_admin/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Invalid");window.location="/myapp/Change_pass_admin/";</Script>''')



def admin_home(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Admin/admin_hm_index.html')

def logout(request):
    request.session['lid']=''
    request.session['lin']='out'
    return redirect('/myapp/login/')



###################################

def view_profile_depo(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vp=Depo_officer.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'Depo Officer/DepoOfficer view profile.html',{'data':vp})


def view_pass_request(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vpr = Pass_req.objects.filter(Status="Pending")
    return render(request,'Depo Officer/DepoOfficer view pass req.html',{'data':vpr})
def view_pass_request_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_date = request.POST['textfield']
    To_Date = request.POST['textfield2']
    ps = Pass_req.objects.filter(Date__range=[From_date, To_Date])
    return render(request,'Depo Officer/DepoOfficer view pass req.html',{'data':ps})

def approve_pass_req(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    apr=Pass_req.objects.filter(id=id).update(Status="Approved")
    return HttpResponse('''<script>alert('Success');window.location="/myapp/view_pass_request/"</script>''')

def reject_pass_req(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    rpr=Pass_req.objects.filter(id=id).update(Status="Rejected")
    return HttpResponse('''<script>alert('Success');window.location="/myapp/view_pass_request/"</script>''')

def view_approved_pass(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vap = Pass_req.objects.filter(Status="Approved")
    return render(request,'Depo Officer/DepoOfficer view approved pass.html',{'data':vap})
def view_approved_pass_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search=request.POST['textfield']
    sa = Pass_req.objects.filter(USERS__Name__icontains=Search)
    return render(request,'Depo Officer/DepoOfficer view approved pass.html',{'data':sa})

def view_rejected_pass(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vrps = Pass_req.objects.filter(Status="Rejected")
    return render(request,'Depo Officer/DepoOfficer view rejected pass.html',{'data':vrps})
def view_rejected_do_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search=request.POST['textfield']
    sr = Pass_req.objects.filter(USERS__Name__icontains=Search)
    return render(request,'Depo Officer/DepoOfficer view rejected pass.html',{'data':sr})


def update_pass(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    up=Updated_pass.objects.all()
    return render(request,'Depo Officer/DepoOfficer update existing pass.html',{'data':up})
def update_pass_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search=request.POST['textfield']
    sup=Updated_pass.objects.filter(PASS_REQ__USERS__Name__icontains=Search)
    return render(request,'Depo Officer/DepoOfficer update existing pass.html',{'data':sup})

def view_prev_pass(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vprv=Pass_req.objects.get(id=id)
    return render(request,'Depo Officer/Depo officer view prev pass.html',{'data':vprv})

def update_pass_date(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    upd=Updated_pass.objects.get(id=id)
    print(id)
    return render(request,'Depo Officer/DepoOfficer udate date.html',{'data':upd})
def update_pass_date_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_date=request.POST['textfield']
    Expiry_date=request.POST['textfield2']
    id=request.POST['id']
    uobj=Updated_pass.objects.get(id=id)
    uobj.Valid_from=From_date
    uobj.Expiry_date=Expiry_date
    uobj.Status="Renewed"
    uobj.save()
    # Pass_req.objects.filter(id=uobj.PASS_REQ_id).update(Time_period=uobj.)
    return HttpResponse('''<script>alert('Success');window.location="/myapp/update_pass/"</script>''')


def view_payments_do(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vp=Payment.objects.filter(PASS_REQ__DEPO_OFFICER__LOGIN_id=request.session['lid'])
    return render(request,'Depo Officer/Depo Officer view Payments.html',{'data':vp})


def view_payments_do_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_date=request.POST['textfield']
    To_date=request.POST['textfield2']
    vps = Payment.objects.filter(Date__range=[From_date, To_date])
    return render(request,'Depo Officer/Depo Officer view Payments.html',{'data':vps})


def view_cancel_req(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Cancel_pass.objects.filter(PASS_REQ__DEPO_OFFICER__LOGIN__id=request.session['lid'],Status="Pending")
    return render(request,"Depo Officer/cancel_request.html",{'data':res})

def view_cancel_req_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    cs=Cancel_pass.objects.filter(PASS_REQ__DEPO_OFFICER__LOGIN__id=request.session['lid'],Status="Pending",Date__range=[from_date,to_date])
    return render(request, "Depo Officer/cancel_request.html", {'data': cs})


def approve_cancel_req(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    crobj=Cancel_pass.objects.filter(id=id).update(Status="Cancelled")
    return HttpResponse('''<script>alert('Success');window.location="/myapp/depo_officer_home/"</script>''')

def view_approved_cancel(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vac = Cancel_pass.objects.filter(Status="Cancelled")
    return render(request,'Depo Officer/DepoOfficer View approved(Cancel).html',{'data':vac})

def delete_approved_cancel_request(request,id):
    vac = Pass_req.objects.get(id=id).delete()
    return redirect('/myapp/view_approved_cancel/')



def view_approved_cancel_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search=request.POST['textfield']
    sac = Cancel_pass.objects.filter(PASS_REQ__USERS__Name__icontains=Search)
    return render(request,'Depo Officer/DepoOfficer View approved(Cancel).html',{'data':sac})


def Change_pass_officer(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Depo Officer/Officer Change Password.html')

def Change_pass_officer_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    oldpass=request.POST['textfield']
    newpass=request.POST['textfield2']  
    confpass=request.POST['textfield3']
    # return HttpResponse('ok')
    res = Login.objects.filter(id=request.session['lid'], password=oldpass)


    if res.exists():
        if newpass == confpass:
            ress = Login.objects.filter(id=request.session['lid'], password=oldpass).update(password=newpass)
            return HttpResponse('''<Script>alert("Password Updated");window.location="/myapp/login/";</Script>''')
        else:
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/myapp/Change_pass_officer/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Invalid");window.location="/myapp/Change_pass_officer/";</Script>''')



def depo_officer_home(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Depo Officer/officer_home_index.html')





######################################

def user_ui(request):
    import datetime
    dty=datetime.date.today()
    dt=str(dty.year-18)+"_"+str(dty.month)+"_"+str(dty.day)
    return render(request,'signup_index.html',{'dt':dt})
def user_ui_post(request):
    Name=request.POST['textfield']
    Gender=request.POST['RadioGroup1']
    Date_of_Birth=request.POST['textfield2']
    Email=request.POST['textfield3']
    Phone_Number=request.POST['textfield4']
    House_name=request.POST['textfield5']
    Place=request.POST['textfield6']
    City=request.POST['textfield7']
    State=request.POST['textfield9']
    Pincode=request.POST['textfield8']
    Photo=request.FILES['fileField']
    Create_Password=request.POST['textfield10']
    Confirm_Password=request.POST['textfield11']

    if Create_Password==Confirm_Password:
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, Photo)
        path = fs.url(date)

        lbj=Login()
        lbj.username=Email
        lbj.password=Create_Password
        lbj.type="user"
        lbj.save()

        uro=Users()
        uro.Name=Name
        uro.Gender=Gender
        uro.Date_of_birth=Date_of_Birth
        uro.Email=Email
        uro.Phone_Number=Phone_Number
        uro.House_Name=House_name
        uro.Place=Place
        uro.City=City
        uro.State=State
        uro.Pincode=Pincode
        uro.Photo=path
        uro.LOGIN=lbj
        uro.save()
        return HttpResponse('''<script>alert('Submitted Successfully');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid Username or Password');window.location="/myapp/user_ui/"</script>''')


def view_user_profile(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vup=Users.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/User view profile.html',{'data':vup})


def edit_user_profile(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    eup=Users.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/User edit profile.html',{'val':eup})

def edit_user_profile_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Name = request.POST['textfield']
    Gender = request.POST['RadioGroup1']
    Date_of_Birth = request.POST['textfield2']
    Email = request.POST['textfield3']
    Phone_Number = request.POST['textfield4']
    House_name = request.POST['textfield7']
    Place = request.POST['textfield6']
    City = request.POST['textfield5']
    State = request.POST['textfield8']
    Pincode = request.POST['textfield9']

    if 'fileField' in request.FILES:
        Photo = request.FILES['fileField']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, Photo)
        path = fs.url(date)

        uro=Users.objects.get(LOGIN_id=request.session['lid'])
        uro.Name=Name
        uro.Gender=Gender
        uro.Date_of_birth=Date_of_Birth
        uro.Email=Email
        uro.Phone_Number=Phone_Number
        uro.House_Name=House_name
        uro.Place=Place
        uro.City=City
        uro.State=State
        uro.Pincode=Pincode
        uro.Photo=path
        uro.save()
        return HttpResponse('''<script>alert('Edited Successfully');window.location="/myapp/view_user_profile/"</script>''')
    else:
        uro = Users.objects.get(LOGIN_id=request.session['lid'])
        uro.Name = Name
        uro.Gender = Gender
        uro.Date_of_birth = Date_of_Birth
        uro.Email = Email
        uro.Phone_Number = Phone_Number
        uro.House_Name = House_name
        uro.Place = Place
        uro.City = City
        uro.State = State
        uro.Pincode = Pincode
        uro.save()
        return HttpResponse('''<script>alert('Edited Successfully');window.location="/myapp/view_user_profile/"</script>''')

def view_officers(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vo=Depo_officer.objects.all()
    return render(request,'User/User view depo officer.html',{'data':vo})
def view_officers_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Search=request.POST['textfield']
    su = Depo_officer.objects.filter(Depo__icontains=Search)
    return render(request,'User/User view depo officer.html',{'data':su})


def pass_request(request,did):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    pr=Charge.objects.all()
    return render(request,'User/User pass req.html',{'data':pr,'did':did})


def calculate(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    From_Place = request.POST['select']
    print(From_Place)
    To_Place = request.POST['select2']
    print(To_Place,"hiiii")
    Time_Period=request.POST['select3']

    print(Time_Period,"Timeeeeeeee")
    Type = request.POST['select4']
    res=Charge.objects.get(From_Place=From_Place,To_Place=To_Place, Type=Type)
    amnt=res.Amouont
    print(amnt)
    if Type=="Normal":
        print(Time_Period)
        if Time_Period== "1 Month" or Time_Period== "1months" :
             print("hh")
             t_amount=float(amnt)*30
        elif Time_Period== "3 Month" or Time_Period== "3months":
            print("hiii")
            t_amount=float(amnt)*90
        elif Time_Period== "6 Month" or Time_Period== "6months":
            print("eee")
            t_amount=float(amnt)*180
    else:
         t_amount=float(amnt)*300
    print(t_amount)
    return JsonResponse({'data':t_amount})




def pass_request_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    did=request.POST['did']
    From_Place = request.POST['select1']
    To_Place = request.POST['select2']
    Type = request.POST['select4']
    # Date=request.POST['textfield2']
    Time_Period=request.POST['select3']
    Amount = request.POST['textfield']


    id_proof = request.FILES['fileField']




    res=Pass_req.objects.filter(USERS__LOGIN__id=request.session['lid'])
    if res.exists():
        return HttpResponse('''<script>alert('You Have Already Request Sended');window.location="/myapp/user_home/"</script>''')
    else:
        probj=Pass_req()
        probj.From_place=From_Place
        probj.To_Place=To_Place
        probj.Type=Type
        from datetime import datetime

        probj.Date=datetime.now().strftime('%Y-%m-%d')
        dt=datetime.now().strftime('%Y%m%d-%H%M%S')+".JPG"

        fs = FileSystemStorage()
        fs.save(dt, id_proof)
        path = fs.url(dt)

        probj.Time_period=Time_Period
        probj.Amouont=Amount
        probj.id_proof=path
        probj.DEPO_OFFICER=Depo_officer.objects.get(id=did)
        probj.USERS=Users.objects.get(LOGIN__id=request.session['lid'])
        probj.Status="pending"
        probj.save()
        return HttpResponse('''<script>alert('Request Sent!');window.location="/myapp/view_status_download/#abc"</script>''')

def view_existing_pass(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')

    if Pass_req.objects.filter(USERS__LOGIN_id=request.session['lid']).exists():

        vpobj=Pass_req.objects.get(USERS__LOGIN_id=request.session['lid'])

        time_period_match = re.search(r'\b(\d+)\s*months?\b', vpobj.Time_period, re.IGNORECASE)
        if time_period_match:
            months = int(time_period_match.group(1))
        else:
            months = 0
        expiration_date = vpobj.Date + datetime.timedelta(days=30 * months)

        context = {
            'data': vpobj,
            'expiration_date': expiration_date,
            'current_date': datetime.date.today(),
        }
        print(vpobj)
        return render(request,'User/User view existing pass.html',context)
    else:
        return HttpResponse('''<script>alert('Request Not Fond!');window.location="/myapp/user_home/"</script>''')



def renew_pass(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Pass_req.objects.get(pk=id)
    return render(request,'User/User Renew Existing Pass.html',{'data':res})

def calculate2(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    print(request.POST)
    id = request.POST['id']
    res1=Pass_req.objects.get(pk=id)
    Time_Period=request.POST['select3']

    print(Time_Period,"Timeeeeeeee")
    res=Charge.objects.get(From_Place=res1.From_place,To_Place=res1.To_Place, Type=res1.Type)
    amnt=res.Amouont
    print(amnt)
    if res1.Type=="Normal":
        if Time_Period== "1months":
             print("hh")
             t_amount=float(amnt)*30
        elif Time_Period== "3months":
            print("hiii")
            t_amount=float(amnt)*90
        elif Time_Period== "6months":
            print("eee")
            t_amount=float(amnt)*180
    else:
         t_amount=float(amnt)*300
    print(t_amount)
    return JsonResponse({'data':t_amount})


def renew_pass_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    id=request.POST['id']
    From_Place = request.POST['select']
    To_Place = request.POST['select2']
    Type = request.POST['select4']
    Time_Period = request.POST['select3']
    Amount = request.POST['textfield']
    rpobj=Pass_req.objects.get(id=id)
    rpobj.From_place=From_Place
    rpobj.To_Place=To_Place
    rpobj.Type=Type
    rpobj.Time_period=Time_Period
    rpobj.Amouont=Amount
    rpobj.Status="Pending"
    rpobj.save()
    return HttpResponse('''<script>window.location="myapp/renew_pass/"</script>''')

def cancel_pass(request,pid):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,"User/Reason.html",{'pid':pid})



def cancel_pass_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    reason=request.POST['textarea']
    pid=request.POST['pid']
    cobj = Cancel_pass()
    cobj.Date = datetime.datetime.now()
    cobj.Status = "Pending"
    cobj.PASS_REQ = Pass_req.objects.get(id=pid)
    cobj.Reason=reason
    cobj.save()
    return HttpResponse('''<script>alert('Request Sent!');window.location="/myapp/user_home/"</script>''')


def payments(request,pid,amnt):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'User/UserPayment.html',{'amnt':amnt,'pid':pid})

def payments_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    pid=request.POST['pid']
    Account_Number=request.POST['textfield']
    IFSC_Code=request.POST['textfield2']
    Holder_Name=request.POST['textfield3']
    Amount=request.POST['textfield4']
    print(Pass_req.objects.get(id=pid).Time_period)
    res=Bank.objects.filter(AccNo=Account_Number,ifsc=IFSC_Code,hoder_name=Holder_Name)
    if res.exists():
        ress = Bank.objects.get(AccNo=Account_Number, ifsc=IFSC_Code, hoder_name=Holder_Name)
        if float(ress.amount)>float(Amount):
            tamount=float(ress.amount)-float(Amount)
            res = Bank.objects.filter(AccNo=Account_Number, ifsc=IFSC_Code, hoder_name=Holder_Name).update(amount=tamount)
            pobj=Payment()
            pobj.Date=datetime.datetime.now()
            pobj.Account_Number=Account_Number
            pobj.Status="paid"
            pobj.Amount=Amount
            pobj.PASS_REQ=Pass_req.objects.get(id=pid)
            pobj.USERS=Users.objects.get(LOGIN__id=request.session['lid'])
            pobj.save()
            if Updated_pass.objects.filter(PASS_REQ_id=pid).exists():
                Updated_pass.objects.filter(PASS_REQ_id=pid).update(Status="Pending")
            else:
                uobj=Updated_pass()
                uobj.Valid_from=datetime.date.today()
                if Pass_req.objects.get(id=pid).Time_period == '1months' or Pass_req.objects.get(id=pid).Time_period == '1 Month':
                    end_date = datetime.date.today() + datetime.timedelta(weeks=4.34524)
                    uobj.Expiry_date = end_date
                elif Pass_req.objects.get(id=pid).Time_period == '3months' or Pass_req.objects.get(id=pid).Time_period == '3 Month':
                    end_date = datetime.date.today() + datetime.timedelta(weeks=13.0357)
                    uobj.Expiry_date = end_date
                elif Pass_req.objects.get(id=pid).Time_period == '6months' or Pass_req.objects.get(id=pid).Time_period == '6 Month':
                    end_date = datetime.date.today() + datetime.timedelta(weeks=26.0715)
                    uobj.Expiry_date = end_date
                elif Pass_req.objects.get(id=pid).Time_period == '12months' or Pass_req.objects.get(id=pid).Time_period == '1 year':
                    end_date = datetime.date.today() + datetime.timedelta(days=365)
                    uobj.Expiry_date = end_date
                uobj.Status = 'Pending'
                uobj.PASS_REQ_id=pid
                uobj.save()
            return HttpResponse('''<script>alert('Payment Successfull');window.location="/user_home/"</script>''')
        else:
            return HttpResponse('''<script>alert('Insufficient Balance');window.location="/myapp/view_status_download/"</script>''')
    else:
        return HttpResponse('''<script>alert('Account Not Found');window.location="/myapp/view_status_download/"</script>''')


def view_status(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')

    if Pass_req.objects.filter(USERS__LOGIN_id=request.session['lid']).exists():

        vs = Pass_req.objects.filter(USERS__LOGIN_id=request.session['lid'])[0]
        vsv='no'
        if Payment.objects.filter(PASS_REQ=vs).exists():
            vsv='yes'
        return render(request,'User/User view status and download.html',{'data':vs, 'data2':vsv})
    return HttpResponse(
        '''<script>alert('No Data');window.location="/myapp/user_home/"</script>''')


def renew_status(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    if Updated_pass.objects.filter(PASS_REQ__USERS__LOGIN_id=request.session['lid']).exists():
        rs=Updated_pass.objects.get(PASS_REQ__USERS__LOGIN_id=request.session['lid'])
        return render(request,'User/User view renew status.html',{'data':rs })
    else:
        return HttpResponse('''<script>alert('Request Not Found');window.location="/myapp/user_home/"</script>''')


def cancel_status(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    if Cancel_pass.objects.filter(PASS_REQ__USERS__LOGIN_id=request.session['lid']).exists():
        cs = Cancel_pass.objects.get(PASS_REQ__USERS__LOGIN_id=request.session['lid'])
        return render(request, 'User/User view cancel status.html', {'data': cs})
    else:
        return HttpResponse('''<script>alert('Request Not Found');window.location="/myapp/user_home/"</script>''')



def complaint(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'User/User Complaint.html')
def complaint_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    complaint=request.POST['textarea']
    cobj=Complaint()
    cobj.Complaints=complaint
    from datetime import datetime
    cobj.Date=datetime.now().strftime('%Y-%m-%d')
    cobj.status="Pending"
    cobj.reply="Pending"
    cobj.USERS=Users.objects.get(LOGIN=request.session['lid'])
    cobj.save()
    return HttpResponse('''<script>alert('Complaint sent');window.location="/myapp/user_home/"</script>''')

def view_reply(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    lid=Users.objects.get(LOGIN=request.session['lid'])
    res=Complaint.objects.filter(USERS_id=lid.id)
    return render(request,'User/User view admin reply.html',{'data':res})
def view_reply_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    lid = Users.objects.get(LOGIN=request.session['lid'])
    res = Complaint.objects.filter(USERS_id=lid.id,Date__range=[from_date,to_date])
    return render(request,'User/User view admin reply.html',{'data':res})

def user_change_pswd(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'User/User Change Password.html')

def user_change_pswd_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    oldpass=request.POST['textfield']
    newpass=request.POST['textfield2']
    confpass=request.POST['textfield3']
    # return HttpResponse('ok')
    res = Login.objects.filter(id=request.session['lid'], password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = Login.objects.filter(id=request.session['lid'], password=oldpass).update(password=newpass)
            return HttpResponse('''<Script>alert("Password Updated");window.location="/myapp/login/";</Script>''')
        else:
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/myapp/user_change_pswd/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Invalid");window.location="/myapp/user_change_pswd/";</Script>''')


def user_view_charges(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    vc=Charge.objects.all()
    return render(request,'User/User View charges.html',{"data":vc})
def user_view_charges_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    from_place = request.POST['textfield']
    to_place=request.POST['textfield2']
    vc2=Charge.objects.filter(From_Place__icontains=from_place,To_Place__icontains=to_place)
    return render(request,'User/User View charges.html',{"data":vc2})


def user_home(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'User/user_hm_index.html')

###################################

def forget_pass(request):
    return render(request,'Forgot pass2.html/')

def forget_pass_post(request):
    email=request.POST['textfield']
    qry = Login.objects.filter(username=email)
    if not qry.exists():
        return HttpResponse('''<Script>alert("User Not Found");window.location="/myapp/login/";</Script>''')

    else:
        import random
        new_pass = random.randint(0000, 9999)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("sktemp85@gmail.com","gmgvakaruinbdamw")  # App Password

        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)

        # Disconnect from the server
        server.quit()
        qryy = Login.objects.filter(username=email).update(password=new_pass)

        return HttpResponse('''<Script>alert("Please Check Your Email");window.location="/myapp/login/";</Script>''')