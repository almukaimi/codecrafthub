from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = "courses.json"

VALID_STATUSES = ["Not Started", "In Progress", "Completed"]

# -----------------------------
# Initialize JSON file
# -----------------------------
def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

# -----------------------------
# Load courses
# -----------------------------
def load_courses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# -----------------------------
# Save courses
# -----------------------------
def save_courses(courses):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(courses, f, indent=4)
        return True
    except:
        return False

# -----------------------------
# Generate ID
# -----------------------------
def get_next_id(courses):
    if not courses:
        return 1
    return max(course["id"] for course in courses) + 1

# -----------------------------
# Validation
# -----------------------------
def validate(data):
    required = ["name", "description", "target_date", "status"]

    for field in required:
        if field not in data or not data[field]:
            return f"Missing field: {field}"

    if data["status"] not in VALID_STATUSES:
        return "Invalid status"

    try:
        datetime.strptime(data["target_date"], "%Y-%m-%d")
    except:
        return "Invalid date format (YYYY-MM-DD required)"

    return None

# -----------------------------
# CREATE course
# -----------------------------
@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.get_json(force=True) or {}

    error = validate(data)
    if error:
        return jsonify({"success": False, "error": error}), 400

    courses = load_courses()

    new_course = {
        "id": get_next_id(courses),
        "name": data["name"],
        "description": data["description"],
        "target_date": data["target_date"],
        "status": data["status"],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    courses.append(new_course)
    save_courses(courses)

    return jsonify({
        "success": True,
        "course": new_course
    }), 201

# -----------------------------
# READ all
# -----------------------------
@app.route("/api/courses", methods=["GET"])
def get_all():
    return jsonify(load_courses()), 200

# -----------------------------
# READ one
# -----------------------------
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_one(course_id):
    courses = load_courses()

    for c in courses:
        if c["id"] == course_id:
            return jsonify(c), 200

    return jsonify({"success": False, "error": "Course not found"}), 404

# -----------------------------
# UPDATE
# -----------------------------
@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update(course_id):
    data = request.get_json(force=True) or {}

    error = validate(data)
    if error:
        return jsonify({"success": False, "error": error}), 400

    courses = load_courses()

    for c in courses:
        if c["id"] == course_id:
            c["name"] = data["name"]
            c["description"] = data["description"]
            c["target_date"] = data["target_date"]
            c["status"] = data["status"]

            save_courses(courses)
            return jsonify({
                "success": True,
                "course": c
            }), 200

    return jsonify({"success": False, "error": "Course not found"}), 404

# -----------------------------
# DELETE
# -----------------------------
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete(course_id):
    courses = load_courses()

    new_courses = [c for c in courses if c["id"] != course_id]

    if len(new_courses) == len(courses):
        return jsonify({"success": False, "error": "Course not found"}), 404

    save_courses(new_courses)

    return jsonify({
        "success": True,
        "message": "Course deleted"
    }), 200

# -----------------------------
# STATS (BONUS FEATURE)
# -----------------------------
@app.route("/api/courses/stats", methods=["GET"])
def get_stats():
    courses = load_courses()

    stats = {
        "total_courses": len(courses),
        "Not Started": 0,
        "In Progress": 0,
        "Completed": 0
    }

    for c in courses:
        status = c.get("status")
        if status in stats:
            stats[status] += 1

    return jsonify({
        "success": True,
        "stats": stats
    }), 200

# -----------------------------
# START APP
# -----------------------------
if __name__ == "__main__":
    init_file()
    app.run(debug=True)