import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("Starting Online Examination System API Verification...")

    # 1. Student CRUD
    print("\n--- Testing Student CRUD ---")
    st_new = {
        "full_name": "Test Student",
        "email": "test@gmail.com",
        "phone": "1234567890",
        "college": "Test College",
        "password": "testpassword"
    }
    r = requests.post(f"{BASE_URL}/students/add/", json=st_new)
    print("Create Student (New):", r.status_code)
    assert r.status_code in [201, 200]
    new_student = r.json()
    new_id = new_student["student_id"]
    print("New Student ID:", new_id)

    # GET list
    r = requests.get(f"{BASE_URL}/students/")
    print("Get Students List:", r.status_code)
    assert r.status_code == 200
    assert len(r.json()) >= 2

    # PUT
    r = requests.put(f"{BASE_URL}/students/update/{new_id}/", json={"phone": "9999999999"})
    print("Update Student Status:", r.status_code)
    assert r.status_code == 200
    assert r.json()["phone"] == "9999999999"

    # DELETE
    r = requests.delete(f"{BASE_URL}/students/delete/{new_id}/")
    print("Delete Student Status:", r.status_code)
    assert r.status_code == 200

    # 2. Exam CRUD
    print("\n--- Testing Examination CRUD ---")
    exam_new = {
        "exam_title": "Java Test",
        "subject": "Java",
        "duration": 45,
        "total_marks": 50,
        "exam_date": "2026-09-01"
    }
    r = requests.post(f"{BASE_URL}/exams/add/", json=exam_new)
    print("Create Exam Status:", r.status_code)
    assert r.status_code in [201, 200]
    new_exam = r.json()
    new_exam_id = new_exam["exam_id"]
    print("New Exam ID:", new_exam_id)

    # GET list
    r = requests.get(f"{BASE_URL}/exams/")
    print("Get Exams List:", r.status_code)
    assert r.status_code == 200
    assert len(r.json()) >= 2

    # PUT
    r = requests.put(f"{BASE_URL}/exams/update/{new_exam_id}/", json={"duration": 50})
    print("Update Exam Status:", r.status_code)
    assert r.status_code == 200
    assert r.json()["duration"] == 50

    # DELETE
    r = requests.delete(f"{BASE_URL}/exams/delete/{new_exam_id}/")
    print("Delete Exam Status:", r.status_code)
    assert r.status_code == 200

    # 3. Question CRUD
    print("\n--- Testing Question CRUD ---")
    quest_new = {
        "exam_title": "Python Programming Test",
        "question": "What is the output of print(type([]))?",
        "option_a": "<class 'dict'>",
        "option_b": "<class 'list'>",
        "option_c": "<class 'tuple'>",
        "option_d": "<class 'set'>",
        "correct_answer": "<class 'list'>",
        "marks": 5
    }
    r = requests.post(f"{BASE_URL}/questions/add/", json=quest_new)
    print("Create Question Status:", r.status_code)
    assert r.status_code in [201, 200]
    new_q = r.json()
    new_q_id = new_q["question_id"]

    # GET
    r = requests.get(f"{BASE_URL}/questions/")
    print("Get Questions List:", r.status_code)
    assert r.status_code == 200

    # PUT
    r = requests.put(f"{BASE_URL}/questions/update/{new_q_id}/", json={"marks": 10})
    print("Update Question Status:", r.status_code)
    assert r.status_code == 200
    assert r.json()["marks"] == 10

    # DELETE
    r = requests.delete(f"{BASE_URL}/questions/delete/{new_q_id}/")
    print("Delete Question Status:", r.status_code)
    assert r.status_code == 200

    # 4. Submission CRUD
    print("\n--- Testing Submission CRUD ---")
    sub_new = {
        "student_name": "Rahul Sharma",
        "exam_title": "Python Programming Test",
        "submitted_answers": "Q1:def,Q2:.py",
        "score": 40
    }
    r = requests.post(f"{BASE_URL}/submissions/add/", json=sub_new)
    print("Create Submission Status:", r.status_code)
    assert r.status_code in [201, 200]
    new_sub = r.json()
    new_sub_id = new_sub["submission_id"]

    # GET
    r = requests.get(f"{BASE_URL}/submissions/")
    print("Get Submissions List:", r.status_code)
    assert r.status_code == 200

    # PUT
    r = requests.put(f"{BASE_URL}/submissions/update/{new_sub_id}/", json={"score": 50})
    print("Update Submission Status:", r.status_code)
    assert r.status_code == 200
    assert r.json()["score"] == 50

    # DELETE
    r = requests.delete(f"{BASE_URL}/submissions/delete/{new_sub_id}/")
    print("Delete Submission Status:", r.status_code)
    assert r.status_code == 200

    # 5. Result CRUD
    print("\n--- Testing Result CRUD ---")
    res_new = {
        "student_name": "Rahul Sharma",
        "exam_title": "Python Programming Test",
        "total_marks": 100,
        "obtained_marks": 80,
        "percentage": 80.0,
        "result_status": "Pass"
    }
    r = requests.post(f"{BASE_URL}/results/add/", json=res_new)
    print("Create Result Status:", r.status_code)
    assert r.status_code in [201, 200]
    new_res = r.json()
    new_res_id = new_res["result_id"]

    # GET
    r = requests.get(f"{BASE_URL}/results/")
    print("Get Results List:", r.status_code)
    assert r.status_code == 200

    # PUT
    r = requests.put(f"{BASE_URL}/results/update/{new_res_id}/", json={"result_status": "Fail"})
    print("Update Result Status:", r.status_code)
    assert r.status_code == 200
    assert r.json()["result_status"] == "Fail"

    # DELETE
    r = requests.delete(f"{BASE_URL}/results/delete/{new_res_id}/")
    print("Delete Result Status:", r.status_code)
    assert r.status_code == 200

    # 6. Auth API Login
    print("\n--- Testing Login Auth API ---")
    login_payload = {
        "email": "rahul@gmail.com",
        "password": "rahul123",
        "role": "student"
    }
    r = requests.post(f"{BASE_URL}/login/", json=login_payload)
    print("Student Login Status:", r.status_code)
    assert r.status_code == 200
    print("Student Login Response:", r.json()["message"])

    login_admin_payload = {
        "email": "admin@examportal.com",
        "password": "admin123",
        "role": "admin"
    }
    r = requests.post(f"{BASE_URL}/login/", json=login_admin_payload)
    print("Admin Login Status:", r.status_code)
    assert r.status_code == 200
    print("Admin Login Response:", r.json()["message"])

    print("\nAPI VERIFICATION SUCCESSFUL! All 20 CRUD + Auth operations completed successfully.")

if __name__ == "__main__":
    test_api()
