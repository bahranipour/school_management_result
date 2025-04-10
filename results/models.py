# results/models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='کاربر')
    parent = models.ForeignKey(User, related_name='children', null=True, blank=True,verbose_name='والدین',on_delete=models.SET_NULL)
    grade = models.CharField(max_length=20,verbose_name='پایه')  # مثال: "پایه دهم"
    student_id = models.CharField(max_length=20, unique=True,verbose_name='کد دانش آموزی')

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.grade}"
    
    

class Subject(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام درس')
    teacher = models.CharField(max_length=100,verbose_name='معلم')

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'
    
    def __str__(self):
        return self.name



class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='دانش آموز')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,verbose_name='درس')
    exam_type = models.CharField(max_length=50,verbose_name='نوع امتحان')  # میانترم، پایان‌ترم
    score = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='نمره')
    date = models.DateField(verbose_name='تاریخ')
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'نتیجه'
        verbose_name_plural = 'نتایج'
    
    def get_grade(self):
        if self.score >= 17: return 'خیلی خوب'
        elif self.score >= 14: return 'خوب'
        elif self.score >= 10: return 'قابل قبول'
        else: return 'نیاز به تلاش'