from django.contrib import admin
from appTwo.models import Topic, Webpage, AccessRecord, User
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
