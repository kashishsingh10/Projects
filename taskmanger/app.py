# from flask import Flask, render_template, request, redirect, session

# app = Flask(__name__)
# app.secret_key = "taskmanager"

# # Store data
# users = {}
# tasks = {}

# @app.route("/")
# def index():
#     return redirect("/login")


# # Registration
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         fullname = request.form["fullname"]
#         email = request.form["email"]
#         username = request.form["username"]
#         password = request.form["password"]
#         confirm = request.form["confirm"]

#         if password == confirm:
#             users[username] = {
#                 "fullname": fullname,
#                 "email": email,
#                 "password": password
#             }
#             tasks[username] = []
#             return redirect("/login")

#     return render_template("register.html")


# # Login
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         if username in users and users[username]["password"] == password:
#             session["user"] = username
#             return redirect("/home")

#     return render_template("login.html")


# # Home
# @app.route("/home", methods=["GET", "POST"])
# def home():
#     if "user" not in session:
#         return redirect("/login")

#     username = session["user"]

#     if request.method == "POST":
#         title = request.form["title"]
#         description = request.form["description"]

#         tasks[username].append({
#             "title": title,
#             "description": description
#         })

#     return render_template(
#         "home.html",
#         username=username,
#         user_tasks=tasks[username]
#     )


# # Update Password
# @app.route("/update-password", methods=["GET", "POST"])
# def update_password():
#     if "user" not in session:
#         return redirect("/login")

#     username = session["user"]

#     if request.method == "POST":
#         old = request.form["old"]
#         new = request.form["new"]
#         confirm = request.form["confirm"]

#         if users[username]["password"] == old and new == confirm:
#             users[username]["password"] = new
#             return redirect("/home")

#     return render_template("update_password.html")


# # Delete Account
# @app.route("/delete-account", methods=["GET", "POST"])
# def delete_account():
#     if "user" not in session:
#         return redirect("/login")

#     username = session["user"]

#     if request.method == "POST":
#         users.pop(username)
#         tasks.pop(username)
#         session.pop("user")
#         return redirect("/login")

#     return render_template("delete_account.html")


# # Logout
# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect("/login")


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, session,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "1234"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class user(db.Model):
    id=db.Column(db.Integer,Primary_key=True)
    email=db.Column(db.String(50),Unique_key=True)
    password=db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(50))

with app.app_context():
    db.create_all()







# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
       username = request.form["username"]
    password = request.form["password"]
    user=user.query.filter_by(username=username,password=password).first()

    if username in users and users[username]["password"] == password:
            session["user"] = username
    return redirect("/home")
    return render_template("login.html")


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]
        if password == confirm:
            users[username] = {
                "fullname": fullname,
                "email": email,
                "password": password
            }
            

        
            return redirect("/login")

    return render_template("register.html")

    new_user =user(
          username=form_username,
          email=form_email,
          password=form_password  
        )
    db.session.add(new_user)
    db.session.commit()
        
        


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect("/home")

    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)















