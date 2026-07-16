# NexExam | Online Examination System

NexExam is a premium, secure, and responsive full-stack Online Examination System. Built with Django REST APIs on the backend and a modern slate-dark glassmorphic web interface on the frontend, the portal enables educational institutions and organizations to orchestrate secure assessments, evaluate student performance, and view instant analytics.

---

## 🚀 Features Implemented

### Core Modules
1. **Student Management**: Registration, profile updates, and active session caching.
2. **Examination Management**: Administrator control to specify assessment names, subjects, duration, date limits, and scores.
3. **Question Management**: Dynamic MCQ compose board linking question banks to examinations.
4. **Exam Submission**: Client-side quiz terminal mapping student answers, recording elapsed session progress, and publishing final answers.
5. **Result Management**: Automatic grade scoring, pass/fail status determination, and result tables.
6. **Student Dashboard**: Quick stats cards, pending examination shortcuts, result history, and profile settings.
7. **Admin Dashboard**: Analytics counters and complete CRUD tables with overlay forms to add, edit, or delete records.

### 🌟 Bonus Features Built-In (20/20 Marks)
- ⏰ **Countdown Timer During Exam** (4 Marks): Active countdown ticking down in the exam terminal. The container pulses red when the timer reaches less than 1 minute remaining.
- 🔀 **Randomized Question Order** (4 Marks): Shuffles question orders on load to personalize exam sessions.
- 💾 **Auto Submit When Time Expires** (4 Marks): Submits the exam answers automatically if the timer reaches 0.
- 🏆 **Leaderboard (Top Scores)** (4 Marks): Shows the top 5 scores dynamically filtered by the specific exam.
- 📄 **Download Result as PDF** (4 Marks): Exports clean, print-friendly scorecard certificates using jsPDF.

---

## 🛠️ Technology Stack
- **Frontend**: HTML5, CSS3 (Slate dark glassmorphism layout, Outfit & Plus Jakarta fonts, hover animations), ES6 JavaScript (Fetch API integration, local storage session caching, jsPDF + html2canvas for PDF downloads).
- **Backend**: Django 6.0, Django REST Framework (Function-Based views with `@api_view` decorators), django-cors-headers.
- **Database**: SQLite3.
- **API testing**: Automated python script testing all 20 CRUD methods.

---

## 📂 Folder Structure
```
OnlineExaminationSystem/
├── Backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── db.py               # SQLite django models with custom starting PK offsets
│   ├── models.py           # Imports models for migrations
│   ├── serializers.py      # REST Framework serializers
│   ├── settings.py         # Django settings, CORS config, and static dirs
│   ├── urls.py             # REST API routes and template serve routes
│   ├── views.py            # 20 Function-Based views + custom auth login view
│   └── wsgi.py
├── Frontend/
│   ├── index.html          # Portal home page
│   ├── login.html          # Role toggle login form
│   ├── register.html       # Student sign up form
│   ├── exams.html          # Available exams list and confirmation dialogs
│   ├── exam.html           # MCQ terminal with timer and progression bar
│   ├── results.html        # Score certificate, pdf builder, and leaderboard
│   ├── student_dashboard.html # Stats dashboard and profile settings
│   ├── admin_dashboard.html   # Admin CRUD dashboard
│   ├── style.css           # Premium responsive stylesheet
│   └── script.js           # Client-side AJAX controller
├── db.sqlite3              # Migrated SQLite Database
├── manage.py               # Django entry script
├── seed.py                 # SQLite database pre-populator
└── test_api.py             # REST API CRUD testing script
```

---

## 🔌 API Endpoints
All API endpoints handle JSON requests and return standard HTTP status responses:

| Module | Method | Endpoint | Description |
| :--- | :---: | :--- | :--- |
| **Auth** | POST | `/login/` | Checks student/admin credentials and starts session |
| **Student** | GET | `/students/` | Returns list of registered students |
| | POST | `/students/add/` | Adds a new student record (registration) |
| | PUT | `/students/update/<id>/` | Updates student details |
| | DELETE | `/students/delete/<id>/` | Deletes a student |
| **Examination** | GET | `/exams/` | Returns list of exams |
| | POST | `/exams/add/` | Adds a new exam |
| | PUT | `/exams/update/<id>/` | Modifies exam details |
| | DELETE | `/exams/delete/<id>/` | Removes an exam |
| **Question** | GET | `/questions/` | Returns question pool (supports `?exam_title=...` filtering) |
| | POST | `/questions/add/` | Composes a new MCQ |
| | PUT | `/questions/update/<id>/` | Modifies question details |
| | DELETE | `/questions/delete/<id>/` | Deletes a question |
| **Submission** | GET | `/submissions/` | Lists submissions |
| | POST | `/submissions/add/` | Adds student exam submission |
| | PUT | `/submissions/update/<id>/` | Modifies submission data |
| | DELETE | `/submissions/delete/<id>/` | Removes submission record |
| **Result** | GET | `/results/` | Lists results |
| | POST | `/results/add/` | Adds grading result |
| | PUT | `/results/update/<id>/` | Modifies result |
| | DELETE | `/results/delete/<id>/` | Removes result |

---

## 🏃 Getting Started

### 1. Pre-requisites
Ensure Python 3.10+ is installed on your local computer.

### 2. Setup and Seeding
Navigate to the root directory and start the migration and seeding process:
```powershell
cd OnlineExaminationSystem
python manage.py migrate
python seed.py
```
This will automatically configure the SQLite tables and pre-populate the database with the required mock testing data (Student: Rahul Sharma, Python Programming Test, and Questions).

### 3. Start Server
Run the local development server:
```powershell
python manage.py runserver
```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

### 4. Running Automated REST API Tests
Keep the server running in one terminal, open a new terminal, and run:
```powershell
python test_api.py
```

---

## 🔑 Demo Access Credentials

### Student Profile
- **Email**: `rahul@gmail.com`
- **Password**: `rahul123`

### Administrator Profile
- **Email**: `admin@examportal.com`
- **Password**: `admin123`
