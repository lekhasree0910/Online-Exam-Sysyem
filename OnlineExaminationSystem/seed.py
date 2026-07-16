import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from Backend.db import Student, Examination, Question, ExamSubmission, Result

# Clear existing
Student.objects.all().delete()
Examination.objects.all().delete()
Question.objects.all().delete()
ExamSubmission.objects.all().delete()
Result.objects.all().delete()

# Create Student
s = Student(
    student_id=101,
    full_name="Rahul Sharma",
    email="rahul@gmail.com",
    phone="9876543210",
    college="ABC Engineering College",
    password="rahul123"
)
s.save()

# Create Exam
e = Examination(
    exam_id=201,
    exam_title="Python Programming Test",
    subject="Python",
    duration=60,
    total_marks=100,
    exam_date="2026-08-15"
)
e.save()

# Create Questions
q1 = Question(
    question_id=301,
    exam_title="Python Programming Test",
    question="Which keyword is used to define a function in Python?",
    option_a="function",
    option_b="def",
    option_c="func",
    option_d="define",
    correct_answer="def",
    marks=20
)
q1.save()

q2 = Question(
    question_id=302,
    exam_title="Python Programming Test",
    question="What is the correct extension for Python files?",
    option_a=".pyt",
    option_b=".py",
    option_c=".pyw",
    option_d=".pyd",
    correct_answer=".py",
    marks=20
)
q2.save()

q3 = Question(
    question_id=303,
    exam_title="Python Programming Test",
    question="Which of the following is an immutable sequence type in Python?",
    option_a="list",
    option_b="dictionary",
    option_c="set",
    option_d="tuple",
    correct_answer="tuple",
    marks=20
)
q3.save()

q4 = Question(
    question_id=304,
    exam_title="Python Programming Test",
    question="Which symbol is used to write comments in Python?",
    option_a="//",
    option_b="/*",
    option_c="#",
    option_d="--",
    correct_answer="#",
    marks=20
)
q4.save()

q5 = Question(
    question_id=305,
    exam_title="Python Programming Test",
    question="What is the output of print(2 ** 3) in Python?",
    option_a="6",
    option_b="8",
    option_c="9",
    option_d="5",
    correct_answer="8",
    marks=20
)
q5.save()

# Create Submission
sub = ExamSubmission(
    submission_id=401,
    student_name="Rahul Sharma",
    exam_title="Python Programming Test",
    submitted_answers="Q1:def,Q2:.py,Q3:tuple,Q4:#,Q5:8",
    score=100
)
sub.save()

# Create Result
r = Result(
    result_id=501,
    student_name="Rahul Sharma",
    exam_title="Python Programming Test",
    total_marks=100,
    obtained_marks=100,
    percentage=100,
    result_status="Pass"
)
r.save()

print("Seeded SQLite database successfully with 1 student, 1 exam, 5 questions, 1 submission, and 1 result.")
