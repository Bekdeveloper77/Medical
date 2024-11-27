from django.contrib import admin
from .models import (Exam,SubMenu,Menu,OnePage,Service,ServiceTop,Patients,Partners,PartnersTop,
                     Appointment, DiseaseType, DoctorSpec, FootetLink,FootetLinkTop,AboutIn,AboutAchive,Specialist,About,DoctorSelf,Medecine, Question,Contact)
# Register your models here.

# Register your models here.
admin.site.register(Question)
admin.site.register(SubMenu)
admin.site.register(Menu)
admin.site.register(Exam)
admin.site.register(OnePage)
admin.site.register(Service)
admin.site.register(ServiceTop)
admin.site.register(Patients)
admin.site.register(Partners)
admin.site.register(PartnersTop)
# admin.site.register(Appointment)
admin.site.register(DiseaseType)
admin.site.register(DoctorSpec)
admin.site.register(FootetLink)
admin.site.register(FootetLinkTop)
admin.site.register(AboutIn)
admin.site.register(AboutAchive)
admin.site.register(Specialist)
admin.site.register(About)
admin.site.register(DoctorSelf)
admin.site.register(Medecine)
admin.site.register(Contact)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'type_of_disease', 'type_of_doctor', 'date', 'admin_message')
    list_filter = ('type_of_disease', 'type_of_doctor', 'date')
    search_fields = ('name', 'phone', 'type_of_disease__name', 'type_of_doctor__name')

    # 'date' maydonini faqat ko'rsatish uchun 'readonly_fields' ga qo'shamiz
    readonly_fields = ('date',)
    fields = ('name', 'phone', 'type_of_disease', 'type_of_doctor', 'message', 'admin_message',
              'date')  # 'date' ko'rinadi, lekin tahrirlanmaydi


admin.site.register(Appointment, AppointmentAdmin)
# admin_message maydonini qo'shish




