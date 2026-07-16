from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve
from . import views

urlpatterns = [
    # Admin Portal
    path('django-admin/', admin.site.urls),

    # Authentication API
    path('login/', views.login_view, name='api_login'),

    # Student APIs
    path('students/add/', views.student_add, name='student_add'),
    path('students/', views.student_list, name='student_list'),
    path('students/update/<int:id>/', views.student_update, name='student_update'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Exam APIs
    path('exams/add/', views.exam_add, name='exam_add'),
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/update/<int:id>/', views.exam_update, name='exam_update'),
    path('exams/delete/<int:id>/', views.exam_delete, name='exam_delete'),

    # Question APIs
    path('questions/add/', views.question_add, name='question_add'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/update/<int:id>/', views.question_update, name='question_update'),
    path('questions/delete/<int:id>/', views.question_delete, name='question_delete'),

    # Exam Submission APIs
    path('submissions/add/', views.submission_add, name='submission_add'),
    path('submissions/', views.submission_list, name='submission_list'),
    path('submissions/update/<int:id>/', views.submission_update, name='submission_update'),
    path('submissions/delete/<int:id>/', views.submission_delete, name='submission_delete'),

    # Result APIs
    path('results/add/', views.result_add, name='result_add'),
    path('results/', views.result_list, name='result_list'),
    path('results/update/<int:id>/', views.result_update, name='result_update'),
    path('results/delete/<int:id>/', views.result_delete, name='result_delete'),

    # Template mappings to serve Frontend pages directly via Django
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('index.html', TemplateView.as_view(template_name='index.html')),
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register.html', TemplateView.as_view(template_name='register.html'), name='register'),
    path('exams.html', TemplateView.as_view(template_name='exams.html'), name='exams'),
    path('exam.html', TemplateView.as_view(template_name='exam.html'), name='exam'),
    path('results.html', TemplateView.as_view(template_name='results.html'), name='results'),
    path('student_dashboard.html', TemplateView.as_view(template_name='student_dashboard.html'), name='student_dashboard'),
    path('admin_dashboard.html', TemplateView.as_view(template_name='admin_dashboard.html'), name='admin_dashboard'),

    # Serve static assets from root for relative URL compatibility
    path('script.js', serve, {'document_root': settings.BASE_DIR / 'Frontend', 'path': 'script.js'}),
    path('style.css', serve, {'document_root': settings.BASE_DIR / 'Frontend', 'path': 'style.css'}),
]
