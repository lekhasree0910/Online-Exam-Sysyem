from rest_framework import serializers
from .db import Student, Examination, Question, ExamSubmission, Result

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'student_id': {'required': False}
        }

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'
        extra_kwargs = {
            'exam_id': {'required': False}
        }

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {
            'question_id': {'required': False}
        }

class ExamSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSubmission
        fields = '__all__'
        extra_kwargs = {
            'submission_id': {'required': False}
        }

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        extra_kwargs = {
            'result_id': {'required': False}
        }
