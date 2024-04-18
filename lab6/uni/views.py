from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student, Course


def students(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        email = request.POST.get('email')
        student = Student.objects.create(first=first , last=last, email=email)
        return redirect('students')

    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'students.html', {'students': students, 'courses': courses})


def courses(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = Course.objects.create(name=name)
        return redirect('courses')

    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
        return redirect('details', student_id=student_id)

    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})