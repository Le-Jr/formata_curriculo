from flask import render_template, Blueprint, request
from app.services.curriculum_service import create_curriculum
from uuid import uuid4

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        create_curriculum(name, email)
        print(f"Nome: {name} email: {email}")

    return render_template('index.html') 