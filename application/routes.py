from application import app, db
from application.models import Rods, Fish
from flask import Flask, render_template, request, redirect, url_for
from application.forms import AddRod, AddFish

@app.route("/")
@app.route("/home")
def home():
    all_rods = Rods.query.all()
    all_fish = Fish.query.all()
    return render_template("index.html", title='home', all_rods=all_fish)

@app.route("/add_rod", methods=["GET","POST"])
def add_rod():
    form = AddRod() 
    if request.method == 'POST':
     if form.validate_on_submit:
        new_rod = Rods(description=form.description.data)
        db.session.add(new_rod)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_rod.html", title="Created Rod", form=form) 

@app.route("/add_fish", methods=["GET","POST"])
def add_fish():
    form = AddFish() 
    if request.method == 'POST':
     if form.validate_on_submit:
        new_fish = Fish(description=form.description.data)
        db.session.add(new_fish)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_fish.html", title="Created Fish", form=form)   

@app.route("/complete/<int:id>")
def complete_rod(id):
    rod_task = Rods.query.filter_by(id=id).first()
    rod_task.completed = True 
    db.session.commit()
    return "Completed Task"

@app.route("/complete/<int:id>")
def complete_fish(id):
    fish_task = Fish.query.filter_by(id=id).first()
    fish_task.completed = True 
    db.session.commit()
    return "Completed Task"


@app.route("/incomplete/<int:id>")
def incomplete_rod(id):
    task = Rods.query.filter_by(id=id).first()
    task.completed - False
    db.session.commit()
    return "Incomplete Task"

@app.route("/incomplete/<int:id>")
def incomplete_fish(id):
    task = Fish.query.filter_by(id=id).first()
    task.completed - False
    db.session.commit()
    return "Incomplete Task"

@app.route("/update_rod/<int:id>", methods=["GET", "POST"])
def update_rod(id):
    form = AddRod()
    rod = Rods.query.filter_by(id=id).first()
    if request.method == "POST": 
        rod.description = rod.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_rod.html", form=form, title="Updated Rods", task=task)

@app.route("/update_fish/<int:id>", methods=["GET", "POST"])
def update_fish(id):
    form = AddFish()
    fish = Fish.query.filter_by(id=id).first()
    if request.method == "POST": 
        fish.description = fish.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_fish.html", form=form, title="Updated Fish", task=task)


@app.route("/delete_rod/<int:id>", methods=["GET","POST"])
def delete_rod(id):
    task = Rods.query.filter_by(id=id).first()
    db.session.delete(rod)
    db.session.commit
    return redirect(url_for("home"))

@app.route("/delete_fish/<int:id>", methods=["GET","POST"])
def delete_fish(id):
    task = Fish.query.filter_by(id=id).first()
    db.session.delete(fish)
    db.session.commit
    return redirect(url_for("home"))  