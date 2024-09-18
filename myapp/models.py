from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Depo_officer(models.Model):
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Date_of_birth=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone_Number=models.CharField(max_length=100)
    Depo=models.CharField(max_length=100,default="")
    Proof=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Users(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_of_birth = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    House_Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100,default="")
    Pincode=models.CharField(max_length=100)
    Photo=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)


class Charge(models.Model):
    From_Place=models.CharField(max_length=100)
    To_Place=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    Amouont=models.CharField(max_length=100)

class Pass_req(models.Model):
    From_place=models.CharField(max_length=100)
    To_Place = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Date = models.DateField()
    Time_period=models.CharField(max_length=100)
    Amouont = models.CharField(max_length=100)
    id_proof=models.CharField(max_length=200,default="")
    Status=models.CharField(max_length=100,default="")
    DEPO_OFFICER=models.ForeignKey(Depo_officer,on_delete=models.CASCADE)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)

class Updated_pass(models.Model):
    PASS_REQ=models.ForeignKey(Pass_req,on_delete=models.CASCADE)
    Valid_from=models.DateField()
    Expiry_date=models.DateField()
    Status=models.CharField(max_length=100)

class Cancel_pass(models.Model):
    PASS_REQ=models.ForeignKey(Pass_req,on_delete=models.CASCADE)
    Date = models.DateField()
    Status=models.CharField(max_length=100)
    Reason=models.CharField(max_length=200,default="")


class Payment(models.Model):
    #Date=models.CharField(max_length=100)
    Date = models.DateField()
    Account_Number=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)
    PASS_REQ=models.ForeignKey(Pass_req,on_delete=models.CASCADE)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)



class Complaint(models.Model):
    # Date=models.CharField(max_length=100)
    Date=models.DateField()
    Complaints=models.CharField(max_length=300)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=200)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)

class Bank(models.Model):
    AccNo=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=100)
    hoder_name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)

