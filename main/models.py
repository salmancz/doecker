from email.mime import application
from optparse import Option
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)

# Association table for User
    
class GI_Association_regestration(models.Model):
    
    Appli_num = models.AutoField(primary_key=True)
    name_of_applicant = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    persons_products_organization_authority = models.CharField(max_length=100)
    type_of_goods = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    name_of_geographical_indications = models.CharField(max_length=100)
    desc_of_goods = models.CharField(max_length=100)
    geo_area = models.CharField(max_length=100)
    proof_of_origin = models.CharField(max_length=100)
    method_of_production = models.CharField(max_length=100)
    uniqueness = models.CharField(max_length=100)
    inspection_body =  models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)
    form_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name_of_applicant

class GI_Assoctiation_renewal(models.Model):
    renewal_num = models.AutoField(primary_key=True)
    name_of_applicant = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_applicant

#public tables for user 

#user table
class GI_User_reges(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class GI_User_renual(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
        


#django user login authentication
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
