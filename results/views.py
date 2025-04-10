# results/views.py
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Result,Student
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger





@login_required
def student_results(request):
    student = get_object_or_404(Student, user=request.user)
    results_list = Result.objects.filter(student=student)
    paginator = Paginator(results_list, 10)
    page_number = request.GET.get('page')  # دریافت شماره صفحه از URL
    
    try:
       results = paginator.page(page_number)
    except PageNotAnInteger:
        results = paginator.page(1)  # اگر صفحه عدد نباشد، صفحه اول نمایش داده شود
    except EmptyPage:
       results = paginator.page(paginator.num_pages) 
    return render(request, 'results/student_results.html', {'results': results,'student':student})




