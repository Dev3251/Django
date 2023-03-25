from django.db import models
from django.utils import timezone
import math  
# from django.templatetags.static import static 

# Create your models here.


class User(models.Model):
    email=models.EmailField(unique=True,max_length=30,blank=False)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    is_active=models.BooleanField(default=False)
    is_verify=models.BooleanField(default=False)
    otp=models.IntegerField(default=456)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=30)
    pic=models.FileField(upload_to="media/upload/chairman",default="media/c_default.png")

    def __str__(self):
        return self.firstname
    

class Societymember(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    block_no=models.CharField(max_length=10)
    occupation=models.CharField(max_length=10)
    ownership=models.CharField(max_length=10)
    dob=models.DateField(max_length=20)
    no_of_familymembers=models.CharField(max_length=2)
    blood_group=models.CharField(max_length=3)
    vehicles_detils=models.CharField(max_length=20)
    pic=models.FileField(upload_to="media/upload/societymember",default="media/s_default.png")


    def __str__(self):
        return self.firstname

class Notice(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount=NoticeViews.objects.filter(notice_id=self.id).count()
        return ncount

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            
            else:
                return str(seconds) + "seconds ago"
        
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minutes ago"
            
            else:
                return str(minutes) + "minutes ago"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hours ago"
            else:
                return str(hours) + "hours ago"
            
        # 1 day to 30 days 
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "days ago"
            else:
                return str(days) + "days ago"
            
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "month ago"
            
        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "year ago"
            
class NoticeViews(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id=models.ForeignKey(Notice,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
class Event(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ecount=EventView.objects.filter(event_id=self.id).count()
        return ecount

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            
            else:
                return str(seconds) + "seconds ago"
        
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minutes ago"
            
            else:
                return str(minutes) + "minutes ago"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hours ago"
            else:
                return str(hours) + "hours ago"
            
        # 1 day to 30 days 
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "days ago"
            else:
                return str(days) + "days ago"
            
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "month ago"
            
        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "year ago"

class EventView(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Complaint(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ccount=ComplaintView.objects.filter(complaint_id=self.id).count()
        return ccount

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            
            else:
                return str(seconds) + "seconds ago"
        
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minutes ago"
            
            else:
                return str(minutes) + "minutes ago"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hours ago"
            else:
                return str(hours) + "hours ago"
            
        # 1 day to 30 days 
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "days ago"
            else:
                return str(days) + "days ago"
            
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "month ago"
            
        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "year ago"


class ComplaintView(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint_id=models.ForeignKey(Complaint,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
