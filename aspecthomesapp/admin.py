from django.contrib import admin
from .models import *
# Register your models here.

class signup(admin.ModelAdmin):
    list_display = ("id","username","email","password","confirmpassword","role")
admin.site.register(user,signup)

class detailpage(admin.ModelAdmin):
    list_display = ("id","u_id","phoneno","address","city","state","country","work_exp","profile_pic","admin_photo")
admin.site.register(detail,detailpage)

class requi(admin.ModelAdmin):
    list_display = ("id","u_id","preferredstyle","submittime","budget","admin_photo","virtual","admin_virtual")
admin.site.register(requirement,requi)

class biddingtable(admin.ModelAdmin):
    list_display = ("id","u_id","requirementid","bidamount","desc","date")
    
admin.site.register(bidding,biddingtable)

class userbooking(admin.ModelAdmin):
    def display_username(self, obj):
        return obj.bid.u_id.username
    list_display = ("id","u_id","display_username","date","totalamount")
    
admin.site.register(booking,userbooking)

class paymenttable(admin.ModelAdmin):
    list_display = ("id","u_id","b_id","paymentdate","mode","status")
admin.site.register(payment,paymenttable)

class cardtable(admin.ModelAdmin):
    list_display = ("id","cname","card_number","expirydate","transaction_id","datetime","balance","cvv")
admin.site.register(card,cardtable)

class addbilling(admin.ModelAdmin):
    list_display = ("id","u_id","book_id","dname","cname","cemail","caddress","city","state","zipcode")
admin.site.register(billing,addbilling)

class virtualtable(admin.ModelAdmin):
    list_display = ("id","u_id","imageupload","description","experience","admin_photo")
admin.site.register(virtual,virtualtable)

class projectable(admin.ModelAdmin):
    list_display = ("id","u_id","project","description")
admin.site.register(project,projectable)

class feedbacktable(admin.ModelAdmin):
    list_display = ("id","u_id","description","submissiondate")
admin.site.register(feedback,feedbacktable)

class newsletteradmin(admin.ModelAdmin):
    list_display = ("id","name","email")
admin.site.register(newsletter,newsletteradmin)

class designertalk(admin.ModelAdmin):
    list_display = ("name","email","phone","subject")
admin.site.register(talkdesigner,designertalk)

class contactusadmin(admin.ModelAdmin):
    list_display = ("id","name","email","subject","message")
admin.site.register(contactus,contactusadmin)