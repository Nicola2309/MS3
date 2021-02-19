import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check for username presence in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_img": request.form.get("user_img")
        }
        mongo.db.users.insert_one(register)

        # Let the user in their session
        session["user"] = request.form.get("username").lower()
        flash("Welcome, Food Lover!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking Username presence in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Stored hashed password must match user's input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if the passwords don't match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Display Username in session using DB data
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if session["user"]:
        return render_template("profile.html", user=user)

    return redirect(url_for("login"))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(user):
    # Update profile function
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": user.lower()})
        submit = {
            "username": user["username"],
            "password": user["password"],
            "user_img": user("user_img"),
        }
        mongo.db.users.update({"_id": ObjectId(user)}, submit)
        flash("Recipe Corrected")

    return render_template("profile.html", user=user)


@app.route("/logout")
def logout():
    # User session cookies removal
    flash("See you soon Chef!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/delete_profile/<username>")
def delete_profile(username):

    mongo.db.users.remove({"username": username.lower()})
    flash("Profile Deleted")
    session.pop("user")

    return redirect(url_for("register"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "difficulty": request.form.get("difficulty"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "preparation": request.form.get("preparation"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Shared!")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    print(recipe)
    return render_template("recipe.html", recipe=recipe)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "difficulty": request.form.get("difficulty"),
            "description": request.form.get("description"),
            "ingredients": request.form.get("ingredients"),
            "preparation": request.form.get("preparation"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Corrected")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("get_recipes"))




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
