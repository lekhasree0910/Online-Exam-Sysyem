from django.db import models
from django.db.models import Max
import datetime

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.student_id:
            max_val = Student.objects.aggregate(Max('student_id'))['student_id__max']
            self.student_id = max_val + 1 if max_val else 101
        super().save(*args, **kwargs)


class Examination(models.Model):
    exam_id = models.IntegerField(primary_key=True, blank=True)
    exam_title = models.CharField(max_length=255, unique=True)
    subject = models.CharField(max_length=255)
    duration = models.IntegerField()  # In minutes
    total_marks = models.IntegerField()
    exam_date = models.DateField()

    def __str__(self):
        return self.exam_title

    def save(self, *args, **kwargs):
        if not self.exam_id:
            max_val = Examination.objects.aggregate(Max('exam_id'))['exam_id__max']
            self.exam_id = max_val + 1 if max_val else 201
        super().save(*args, **kwargs)


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, blank=True)
    exam_title = models.CharField(max_length=255)
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.exam_title} - Q{self.question_id}"

    def save(self, *args, **kwargs):
        if not self.question_id:
            max_val = Question.objects.aggregate(Max('question_id'))['question_id__max']
            self.question_id = max_val + 1 if max_val else 301
        super().save(*args, **kwargs)


class ExamSubmission(models.Model):
    submission_id = models.IntegerField(primary_key=True, blank=True)
    student_name = models.CharField(max_length=255)
    exam_title = models.CharField(max_length=255)
    submitted_answers = models.TextField()  # comma separated or custom string format: "Q1:a,Q2:b"
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.submission_id} by {self.student_name}"

    def save(self, *args, **kwargs):
        if not self.submission_id:
            max_val = ExamSubmission.objects.aggregate(Max('submission_id'))['submission_id__max']
            self.submission_id = max_val + 1 if max_val else 401
        super().save(*args, **kwargs)


class Result(models.Model):
    result_id = models.IntegerField(primary_key=True, blank=True)
    student_name = models.CharField(max_length=255)
    exam_title = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    percentage = models.FloatField()
    result_status = models.CharField(max_length=50)  # Pass or Fail

    def __str__(self):
        return f"Result {self.result_id} for {self.student_name}"

    def save(self, *args, **kwargs):
        if not self.result_id:
            max_val = Result.objects.aggregate(Max('result_id'))['result_id__max']
            self.result_id = max_val + 1 if max_val else 501
        super().save(*args, **kwargs)
