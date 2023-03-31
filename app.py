import random
import string

from flask import Flask, render_template, flash, redirect, url_for
from forms import *
from models import *
from config import *


def generate_password(length):
    special_chars = "!@#$%^&*()_+"
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    password = ""

    # Add at least one of each character type
    password += random.choice(special_chars)
    password += random.choice(digits)
    password += random.choice(lowercase)
    password += random.choice(uppercase)

    # Add remaining characters
    for _ in range(length-4):
        password += random.choice(special_chars +
                                  digits + lowercase + uppercase)

    # Shuffle the password to make it more random
    password = ''.join(random.sample(password, len(password)))

    return password


@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.generate_password.data:
            password_length = int(form.password_length.data)
            password = generate_password(password_length)
            return render_template("index.html", form=form, password=password)
        else:
            password = form.password.data
        new_user = User(email=form.email.data, password=password)
        db.session.add(new_user)
        db.session.commit()
        if form.submit.data:
            flash("User successfully registered", 'success')
        return redirect(url_for("home"))
    return render_template('index.html', form=form)


@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route('/user/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("users"))


if __name__ == '__main__':
    app.run()
