# forms.py

from django import forms
from .models import Student, Course, Score

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
    def add_student(request):
        student = super().save(commit=False)
        if request: 
            student.save()
        return student
    
class CourseForm(forms.ModelForm):
    class Meta:
        # Specifies the model to use for the form 
        model = Course

class ScoreForm(forms.ModelForm):
    class Meta:
        # Specifies the model to use for the form 
        model = Score