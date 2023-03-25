from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Chairman)
admin.site.register(Societymember)
admin.site.register(Notice)
admin.site.register(NoticeViews)
admin.site.register(Event)
admin.site.register(EventView)
admin.site.register(Complaint)
admin.site.register(ComplaintView)
