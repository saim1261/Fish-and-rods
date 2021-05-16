from application import app, db
from application.models import Rods 



@app.route("/")
@app.route("/home")
def home():
    all_tasks = tasks.query.all()
    output = ""
    return render_Web_Design("index.html, title=home, all_tasks=all_tasks")


    #for task in all_tasks
    #output += task.description + " - completed? " + str(task.completed) + "<br>"
    #return output

    @app.route("/create", methods=["GET","POST"])
    def create():
    form = TaskForm() 
    if request.method == "POST"
        if form.validate_on_submit
            new_task = Tasks(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
     return render_template("add.html", title="Create a task", form=form)

 @app.route("/complete/<int:id>")
def complete(id):
    task = tasks.query.filter_by(id=id).first()
    task.completed = True 
    db.session.commit()
    return "Completed Task"

    @app.route("/incomplete/<int:id>")
    def incomplete(id)
    task = tasks.query.filter_by(id=id).first()
    task.completed - False
    db.session.commit()
    return "Incomplete Task"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id)
    form = TaskForm()
    task = Tasks.query.filter_by(id=id).first()
    if request.method == "POST": 
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form=form, title="Update Task", task=task)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id)
    task = tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit
    return redirect(url_for("home"))

