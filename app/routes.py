from flask import render_template, Blueprint, request
from app.services.curriculum_service import create_curriculum
from uuid import uuid4

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        celphone = request.form.get("celphone")
        experience = request.form.get("experience")
        resume = request.form.get("resume")


        create_curriculum(name, email, celphone, experience, resume)
        print(f"Nome: {name} email: {email} Celular: {celphone} experiência: {experience} resumo: {resume}")

    return render_template('index.html') 