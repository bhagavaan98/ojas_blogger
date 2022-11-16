from django.contrib import admin
from . models import Contact,blog
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','country','address']

@admin.register(blog)
class logAdmin(admin.ModelAdmin):
    list_display=['id','title','content']


