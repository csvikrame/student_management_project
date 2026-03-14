from django.db import models


class Student(models.Model):
    SEX_CHOICES = (
        ('m', 'Masculin'),
        ('f', 'Féminin'),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    students = models.ManyToManyField(
        Student,
        through='Score',
        related_name='courses'
    )

    def __str__(self):
        return self.name


class Score(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='scores'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='scores'
    )
    score = models.FloatField()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} - {self.course.name} : {self.score}"