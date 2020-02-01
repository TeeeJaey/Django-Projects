from django.db import models
from tastypie.resources import ModelResource
from MainApp.models import User,AccessRecord

class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'Users'


class AccessRecordResource(ModelResource):
    
    class Meta:
        queryset = AccessRecord.objects.all()
        resource_name = 'AccessRecords'

