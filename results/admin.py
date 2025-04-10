from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import Student, Subject, Result

# ثبت مدل Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'student_id', 'parent_info')
    list_filter = ('grade',)
    search_fields = ('user__first_name', 'user__last_name', 'student_id')
    
    def parent_info(self, obj):
        return obj.parent.get_full_name() if obj.parent else "ندارد"
    parent_info.short_description = 'والدین'

# ثبت مدل Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name', 'teacher')

# ثبت مدل Result
@admin.register(Result)
class ResultAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ('student', 'subject', 'exam_type', 'score', 'grade', 'date')
    list_filter = ('exam_type', 'subject', 'date')
    search_fields = ('student__user__first_name', 'student__user__last_name')
    
    raw_id_fields = ('student',)  # نمایش به صورت جستجوگر پیشرفته

    fieldsets = (
    ('اطلاعات پایه', {
        'fields': ('student', 'subject', 'date')
    }),
    ('نمره‌دهی', {
        'fields': ('exam_type', 'score')
    }),
    )
    
    def grade(self, obj):
        return obj.get_grade()
    grade.short_description = 'نمره'


