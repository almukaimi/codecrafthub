

## 📌 Project Overview

CodeCraftHub is a simple REST API-based learning management system built using Python and Flask. It allows users to manage and track learning courses they want to complete.

The system uses **JSON file storage instead of a database**, making it beginner-friendly and ideal for learning REST API fundamentals.

---

## ✨ Features

- Create new courses
- View all courses
- View a specific course
- Update course details and status
- Delete courses
- JSON-based storage (no database required)
- RESTful API design
- Input validation
- Error handling for invalid requests

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd CodeCraftHub
2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
▶️ Run the Application
python app.py

The server will run at:

http://127.0.0.1:5000
🔗 API Endpoints
1. Create Course

POST /api/courses

{
  "name": "Python Basics",
  "description": "Learn Python fundamentals",
  "target_date": "2026-12-31",
  "status": "Not Started"
}
2. Get All Courses

GET /api/courses

3. Get Course by ID

GET /api/courses/<id>

Example:

/api/courses/1
4. Update Course

PUT /api/courses/<id>

{
  "name": "Updated Course",
  "description": "Updated description",
  "target_date": "2026-11-30",
  "status": "In Progress"
}
5. Delete Course

DELETE /api/courses/<id>

🧪 Testing the API

Use curl commands:

Create course
curl -X POST http://127.0.0.1:5000/api/courses \
-H "Content-Type: application/json" \
-d '{
  "name": "Test Course",
  "description": "Testing API",
  "target_date": "2026-12-31",
  "status": "Not Started"
}'
Get all courses
curl http://127.0.0.1:5000/api/courses
Get single course
curl http://127.0.0.1:5000/api/courses/1
Update course
curl -X PUT http://127.0.0.1:5000/api/courses/1 \
-H "Content-Type: application/json" \
-d '{
  "name": "Updated Course",
  "description": "Updated description",
  "target_date": "2026-11-30",
  "status": "In Progress"
}'
Delete course
curl -X DELETE http://127.0.0.1:5000/api/courses/1
⚠️ Error Handling Examples
Missing field
curl -X POST http://127.0.0.1:5000/api/courses \
-H "Content-Type: application/json" \
-d '{
  "name": "Bad Course"
}'
Invalid status
curl -X POST http://127.0.0.1:5000/api/courses \
-H "Content-Type: application/json" \
-d '{
  "name": "Test",
  "description": "Test",
  "target_date": "2026-12-31",
  "status": "Finished"
}'
Course not found
curl http://127.0.0.1:5000/api/courses/999
📁 Project Structure
CodeCraftHub/
│
├── app.py              # Flask application (main API)
├── courses.json       # JSON storage file
├── requirements.txt   # Dependencies
└── README.md          # Documentation
🎯 Summary

This project demonstrates:

REST API development using Flask
CRUD operations
File-based JSON storage
Input validation
Error handling
Backend fundamentals for beginners
