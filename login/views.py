from django.shortcuts import render
from .models import page 
def login(request):
    if request.method == "POST":
        # data = request.POST

        student_name = request.POST.get('student_name')
        student_Rollno = request.POST.get('student_Rollno')
        student_course = request.POST.get('student_course')
        student_email = request.POST.get('student_email')

                
    
        page.objects.create(
              student_name=student_name,
              student_Rollno=student_Rollno,
              student_course=student_course,
              student_email=student_email,
            )
               
    return render(request, 'login.html')
