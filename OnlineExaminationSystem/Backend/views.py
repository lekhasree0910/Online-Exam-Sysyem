from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .db import Student, Examination, Question, ExamSubmission, Result
from .serializers import (
    StudentSerializer, ExaminationSerializer, QuestionSerializer,
    ExamSubmissionSerializer, ResultSerializer
)

# ----------------- Student APIs -----------------

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def student_add(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def student_update(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def student_delete(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)


# ----------------- Examination APIs -----------------

@api_view(['GET'])
def exam_list(request):
    exams = Examination.objects.all()
    serializer = ExaminationSerializer(exams, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def exam_add(request):
    serializer = ExaminationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def exam_update(request, id):
    try:
        exam = Examination.objects.get(pk=id)
    except Examination.DoesNotExist:
        return Response({"error": "Examination not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ExaminationSerializer(exam, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def exam_delete(request, id):
    try:
        exam = Examination.objects.get(pk=id)
    except Examination.DoesNotExist:
        return Response({"error": "Examination not found"}, status=status.HTTP_404_NOT_FOUND)
    
    exam.delete()
    return Response({"message": "Examination deleted successfully"}, status=status.HTTP_200_OK)


# ----------------- Question APIs -----------------

@api_view(['GET'])
def question_list(request):
    questions = Question.objects.all()
    # Support filtering by exam_title if query parameter is provided
    exam_title = request.query_params.get('exam_title')
    if exam_title:
        questions = questions.filter(exam_title=exam_title)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def question_add(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def question_update(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = QuestionSerializer(question, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def question_delete(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
    
    question.delete()
    return Response({"message": "Question deleted successfully"}, status=status.HTTP_200_OK)


# ----------------- Exam Submission APIs -----------------

@api_view(['GET'])
def submission_list(request):
    submissions = ExamSubmission.objects.all()
    serializer = ExamSubmissionSerializer(submissions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def submission_add(request):
    serializer = ExamSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def submission_update(request, id):
    try:
        submission = ExamSubmission.objects.get(pk=id)
    except ExamSubmission.DoesNotExist:
        return Response({"error": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ExamSubmissionSerializer(submission, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def submission_delete(request, id):
    try:
        submission = ExamSubmission.objects.get(pk=id)
    except ExamSubmission.DoesNotExist:
        return Response({"error": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)
    
    submission.delete()
    return Response({"message": "Submission deleted successfully"}, status=status.HTTP_200_OK)


# ----------------- Result APIs -----------------

@api_view(['GET'])
def result_list(request):
    results = Result.objects.all()
    serializer = ResultSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def result_add(request):
    serializer = ResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def result_update(request, id):
    try:
        result = Result.objects.get(pk=id)
    except Result.DoesNotExist:
        return Response({"error": "Result not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ResultSerializer(result, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def result_delete(request, id):
    try:
        result = Result.objects.get(pk=id)
    except Result.DoesNotExist:
        return Response({"error": "Result not found"}, status=status.HTTP_404_NOT_FOUND)
    
    result.delete()
    return Response({"message": "Result deleted successfully"}, status=status.HTTP_200_OK)


# ----------------- Auth API -----------------

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')
    
    if not email or not password or not role:
        return Response({"error": "Please provide email, password, and role"}, status=status.HTTP_400_BAD_REQUEST)
    
    if role == 'admin':
        if email == 'admin@examportal.com' and password == 'admin123':
            return Response({
                "message": "Admin login successful",
                "user": {
                    "email": email,
                    "role": "admin",
                    "full_name": "System Administrator"
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Admin credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
    elif role == 'student':
        try:
            student = Student.objects.get(email=email, password=password)
            serializer = StudentSerializer(student)
            return Response({
                "message": "Student login successful",
                "user": {
                    **serializer.data,
                    "role": "student"
                }
            }, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Invalid Student credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
    return Response({"error": "Invalid role specified"}, status=status.HTTP_400_BAD_REQUEST)
