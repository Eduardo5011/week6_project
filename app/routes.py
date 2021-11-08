# from flask import render_template, request, redirect, url_for, flash

# from app import app
# from .forms import LoginForm, RegisterForm
# from .models import User
# from flask_login import login_user, current_user, logout_user, login_required



# @app.route('/')
# @login_required
# def index():
#     return render_template('index.html.j2')

# @app.route('/students', methods=['GET']) 
# @login_required
# def students():
#     my_students = {"Eduardo", "Jackie", "ceelo", "Narles"}
#     return  render_template('students.html.j2', students=my_students)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         #do Login stuff
#         email = request.form.get("email").lower()
#         password = request.form.get("password")
                                
#         u = User.query.filter_by(email=email).first()

#         if u and u.check_hashed_password(password):
#             login_user(u)
#             flash('You have logged in', 'success')
#             return redirect(url_for("index"))
#         error_string = "Invalid Email password combo"
#         return render_template('login.html.j2', error = error_string, form=form)
#     return render_template('login.html.j2', form=form)

# @app.route('/logout')
# @login_required
# def logout():
#     if current_user:
#         logout_user()
#         flash('You have logged out', 'danger')
#         return redirect(url_for('login'))



# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm() 
#     if request.method == 'POST' and form.validate_on_submit():
#         try:
#             new_user_data = {
#                     "first_name":form.first_name.data.title(),
#                     "last_name":form.last_name.data.title(),
#                     "email":form.email.data.lower(),
#                     "password": form.password.data
#             }     
#             new_user_object = User()
#             new_user_object.from_dict(new_user_data)
#             new_user_object.save()
#         except:
#             error_string = "There was an unexpected Error creating your account. Please try again" 
#             return render_template('register.html.j2', form=form, error=error_string)
#         return redirect(url_for('login'))
#     return render_template('register.html.j2', form=form)