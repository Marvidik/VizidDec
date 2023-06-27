from django.contrib import admin
from .models import Contact,Products,Newsletter,Work,Pictures

# Register your models here.
admin.site.register(Contact)
admin.site.register(Products)
admin.site.register(Newsletter)
admin.site.register(Work)
admin.site.register(Pictures)