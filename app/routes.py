from flask import redirect, render_template, Blueprint, request, send_file, send_from_directory, url_for
from app.services.curriculum_service import create_curriculum
from uuid import uuid4
from .curriculum_form import generate_curriculum

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
        
        pdf_path = generate_curriculum(name, email, celphone, experience, resume)
        # print(f"PDF gerado em: {pdf_path}")
        # redirect = url_for('download')

    return render_template('index.html')


@main.route("/download/<pdf_path>")
def download(pdf_path):
    return send_from_directory(pdf_path, as_attachment=True)