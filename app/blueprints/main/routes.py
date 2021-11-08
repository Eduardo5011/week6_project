from flask import render_template, request


from flask_login import login_required
from .import bp as main



@main.route('/')
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/students', methods=['GET']) 
@login_required
def students():
    my_students = {"Eduardo", "Jackie", "ceelo", "Narles"}
    return  render_template('students.html.j2')

 

    