from flask import render_template, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from .import bp as auth



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        #do Login stuff
        email = request.form.get("email").lower()
        password = request.form.get("password")
                                
        u = User.query.filter_by(email=email).first()

        if u and u.check_hashed_password(password):
            login_user(u)
            flash('You have logged in', 'success')
            return redirect(url_for("main.index"))
        error_string = "Invalid Email password combo"
        return render_template('login.html.j2', error = error_string, form=form)
    return render_template('login.html.j2', form=form)

@auth.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have logged out', 'danger')
        return redirect(url_for('auth.login'))



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm() 
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data = {
                    "first_name":form.first_name.data.title(),
                    "last_name":form.last_name.data.title(),
                    "email":form.email.data.lower(),
                    "password": form.password.data
            }     
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
            new_user_object.save()
        except:
            error_string = "There was an unexpected Error creating your account. Please try again" 
            return render_template('register.html.j2', form=form, error=error_string)
        return redirect(url_for('auth.login'))
    return render_template('register.html.j2', form=form)