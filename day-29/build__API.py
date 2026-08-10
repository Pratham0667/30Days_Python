from flask import Flask, Response, request
import os
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from dotenv import load_dotenv

app = Flask(__name__)

# Load .env
load_dotenv()

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI")

client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]


# -----------------------------------
# GET ALL STUDENTS
# -----------------------------------

@app.route("/api/v1.0/students", methods=["GET"])
def get_student():

    students = list(db.students.find({}, {"_id": 0}))

    return Response(
        dumps(students),
        mimetype="application/json"
    )


# -----------------------------------
# GET SINGLE STUDENT
# -----------------------------------

@app.route("/api/v1.0/students/<id>", methods=["GET"])
def single_student(id):

    student = db.students.find_one({
        "_id": ObjectId(id)
    })

    return Response(
        dumps(student),
        mimetype="application/json"
    )


# -----------------------------------
# CREATE STUDENT
# -----------------------------------

@app.route("/api/v1.0/students", methods=["POST"])
def create_student():

    name = request.form["name"]
    country = request.form["country"]
    city = request.form["city"]
    skills = request.form["skills"].split(", ")
    bio = request.form["bio"]
    birthyear = request.form["birthyear"]

    created_at = datetime.now()

    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "created_at": created_at
    }

    db.students.insert_one(student)

    return Response(
        dumps({"result": "student created"}),
        mimetype="application/json"
    )


# -----------------------------------
# UPDATE STUDENT
# -----------------------------------

@app.route("/api/v1.0/students/<id>", methods=["PUT"])
def update_student(id):

    query = {
        "_id": ObjectId(id)
    }

    name = request.form["name"]
    country = request.form["country"]
    city = request.form["city"]
    skills = request.form["skills"].split(", ")
    bio = request.form["bio"]
    birthyear = request.form["birthyear"]

    created_at = datetime.now()

    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "created_at": created_at
    }

    db.students.update_one(
        query,
        {"$set": student}
    )

    return Response(
        dumps({"result": "the student has been updated"}),
        mimetype="application/json"
    )


# -----------------------------------
# DELETE STUDENT
# -----------------------------------

@app.route("/api/v1.0/students/<id>", methods=["DELETE"])
def delete_student(id):

    db.students.delete_one({
        "_id": ObjectId(id)
    })

    return Response(
        dumps({"result": "the student has been deleted"}),
        mimetype="application/json"
    )


# -----------------------------------
# RUN SERVER
# -----------------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5167))

    app.run(
        debug=True,
        host="0.0.0.0",
        port=port
    )