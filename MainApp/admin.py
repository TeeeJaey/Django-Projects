from django.contrib import admin
from MainApp.models import AccessRecord,Topic,Webpage,User
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)


