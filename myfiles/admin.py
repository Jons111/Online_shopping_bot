from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminMax(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','rasm','tur','malumot']

admin.site.register(Maxsulot,AdminMax)


class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi',]

admin.site.register(Type,AdminType)


class AdminKorzinka(admin.ModelAdmin):
    list_display = ['id','tg_id','ism','nomi','narxi','rasm','son',]

admin.site.register(Korzinka,AdminKorzinka)