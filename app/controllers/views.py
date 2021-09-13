from flask import request
from flask import render_template, redirect, url_for, flash

from app.controllers import bp
from app.models import db
from app.models.forms import RegisterForm
from app.models.tables import User


@bp.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        address = f"{form.address_street.data} {form.address_number.data} - {form.address_complement.data} | {form.address_cep.data}"
        user = User(
            form.name.data,
            form.email.data,
            form.phone.data,
            address
        )

        try:
            db.session.add(user)
            db.session.commit()
        except Exception:
            print("Não foi possível")
        
        return redirect(url_for('views.index'))

    if form.errors != {}:
        for list_msg in form.errors.values():
            for err_msg in list_msg:
                flash(err_msg, "danger")

    return render_template("index.html", form=form)


@bp.route("/users", methods=["GET", "POST"])
def users():
    form = RegisterForm()

    if form.validate_on_submit():
        address = f"{form.address_street.data} {form.address_number.data} - {form.address_complement.data} | {form.address_cep.data}"

        user = User.query.filter_by(email=form.email.data).first()
        user.name = form.name.data
        user.address = address
        db.session.commit()

    if form.errors != {}:
        for list_msg in form.errors.values():
            for err_msg in list_msg:
                flash(err_msg, "danger")

    users = User.query.all()
    return render_template("users.html", users=users, form=form)


@bp.route("/users/remove", methods=["GET", "POST"])
def remove_user():
    req = request.get_json()
    user = User.query.filter_by(id=req["user"])

    if user:
        user.delete()
        db.session.commit()

    return redirect(url_for("views.users"))