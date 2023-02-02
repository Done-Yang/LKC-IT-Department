from django.contrib import admin
from .models import StudentExtra,TeacherExtra,Notice,CustomUser,SessionYear,StaffExtra
# Register your models here. (by Mikealson Academy.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser)
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_id']
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

admin.site.register(SessionYear)
admin.site.register(StaffExtra)
