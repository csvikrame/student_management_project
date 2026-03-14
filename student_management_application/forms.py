# forms.py

from django import forms
from django.shortcuts import redirect, render
from .models import Student, Course, Score


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'sex']

    def add_student(request):
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        else:
            form = StudentForm()

        return render(request, 'add_student.html', {'form': form})
    
    def student_list(request):
        students = Student.objects.all()
        return render(request, 'student_list.html', {'students': students})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher']

    def course_list(request):
        courses = Course.objects.all()
        return render(request, 'course_list.html', {'courses': courses})


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student', 'course', 'score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personnalisation des widgets
        self.fields['student'].widget.attrs.update({'class': 'form-control'})
        self.fields['course'].widget.attrs.update({'class': 'form-control'})
        self.fields['score'].widget.attrs.update({'class': 'form-control'})

    def score_list(request):
        scores = Score.objects.all()
        return render(request, 'score_list.html', {'scores': scores})