from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Order)
admin.site.register(Tag)