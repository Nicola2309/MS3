import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from math import ceil
if os.path.exists("env.py"):
    import env


# ------- Configuration -------
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------- Checking User Function -------
def actual_user(username):
    if "user" in session.keys():
        if session["user"] == username:
            return True

    return False


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# ------- Recipes Page -------


@app.route("/get_recipes/")
def get_recipes():

    """
     Gets all the recipes from the database
     Returns:
     template: recipes.html

    """

    recipes = list(mongo.db.recipes.find())

    return render_template("recipes.html", recipes=recipes)


@app.route('/search_recipes/<query>', methods=['GET', 'POST'])
def search_recipes(query):

    """
     Allows the User to Search recipes by name or category
     Returns:
     template: recipes.html with filtered options

    """
    # search Recipes function
    if search:
        recipes = list(
            mongo.db.recipes.find({"category_name": query}))

    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
     Allows the User to Search recipes by category
     clicking the btns
     Returns:
     template: recipes.html with filtered options

    """
    # Search Buttons function
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# ------- Register Page -------


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows the registration of the user rendering the
    register.html page and sending the data to the MongoDb database

    Prevents the upload of the same username if already in DataBase

    """
    if request.method == "POST":
        # check for username presence in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # prevent username multiplication
        if existing_user:
            flash("This username already taken, try with a new one!")
            return redirect(url_for("register"))

        # Elaborates data from the form sending it to the user collection
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_img": request.form.get("user_img")
        }
        mongo.db.users.insert_one(register)

        # Welcomes and Lets the user in their session
        session["user"] = request.form.get("username").lower()
        flash("Welcome, Food Lover!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# ------- Login Page -------


@app.route("/login", methods=["GET", "POST"])
def login():

    """
    Allows the login of the user into their account,
    rendering the
    register.html page and sending the data to the MongoDb database

    Prevents the upload of the same username if already in DataBase

    """
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
                flash("Welcome back, {}".format(request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if the passwords don't match
                flash("Incorrect Username and/or Password, try again")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password, try again")
            return redirect(url_for("login"))

    return render_template("login.html")


# ------- Logout Page -------


# registered user logout function
@app.route("/logout")
def logout():
    flash("See you soon Chef!")
    # User session cookies removal
    session.pop("user")
    return redirect(url_for("login"))


# ------- Profile Page -------


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    """
    Renders profile html page with the user information of the logged user,
    retireves from MongDB the user information and the recipes
    uploaded by the user using pagination and a limit of 6 per page

    """

    # Display Username in session using DB data
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if not actual_user(username.lower()):
        return redirect(url_for("login"))

    if "user" in session.keys():
        if session["user"] == username:
            recipes = list(
                mongo.db.recipes.find({"created_by": username.lower()}))

        # page number fetching
        page = int(request.args.get('page') or 1)
        num = 6

        # count instances for pagination
        count = ceil(float(len(recipes) / num))

        # page -1 to check if the first items are found
        start = (page - 1) * num
        finish = start + num
        show_recipes = recipes[start:finish]

        return render_template(
            "profile.html", user=user, recipes=show_recipes,
            page=page, count=count, search=False)
    else:
        return redirect(url_for("login"))

    return render_template(
        "profile.html", user=user, recipes=recipes
    )


# ------- Edit Profile Page -------


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):

    """
    Checks for the username field to allow only the owner of the profile to
    modify it.
    Allows the user to update thier profile through a form, when submitted
    sends the new data to the database and updates the profile fields


    """

    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if not actual_user(username.lower()):
        return redirect(url_for("login"))

    # Update profile function
    if request.method == "POST":
        submit = {
            "username": user["username"],
            "email": request.form.get("email"),
            "password": user["password"],
            "user_img": request.form.get("user_img"),
        }
        mongo.db.users.update({"username": session["user"]}, submit)
        flash("Profile Updated!")

        return render_template("profile.html", user=user)

    if "user" in session:
        return render_template("edit_profile.html", user=user)

    return redirect(url_for("login"))


# ------- Articles Page -------


@app.route("/articles")
def articles():
    # Renders the articles.html page
    return render_template("articles.html")


# ------- Delete Profile function -------


@app.route("/delete_profile/<username>")
def delete_profile(username):

    """
    This function allows the user to delete their account,
    sends a flash message that confirms the deletion and remove the user
    from the logged session

    """

    mongo.db.users.remove({"username": username.lower()})
    flash("Profile Deleted")
    session.pop("user")

    return redirect(url_for("register"))


# ------- Add Recipe Page -------


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    The registered user can upload a recipe to the website,
    checking that the user is logged in and preventing a casual user to upload
    recipes.
    A security feature learnt from my fellow
    student work https://github.com/AudreyLL88/MS3__Sante/blob/master/app.py

    """

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "difficulty": request.form.get("difficulty"),
            "servings": request.form.get("servings"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "recipe_image": request.form.get("recipe_image"),
            "image_source": request.form.get("image_source"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Shared!")
        return redirect(url_for("get_recipes"))

    # checking if the user is in session
    if "user" in session:
        user = session["user"].lower()

        if user == session["user"].lower():
            return render_template("add_recipe.html")

        # prevent the access to other users as well
        else:
            return redirect(url_for("home"))

    else:
        return redirect(url_for("login"))


# ------- Single Recipe Page -------


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):

    """
    Renders the recipe page that the user wants to see through
    the ObjectId.

    """

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    print(recipe)
    return render_template("recipe.html", recipe=recipe)


# ------- Edit Recipe Page -------


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    """
    Allows the user to edit the previously uploaded recipes getting
    the form they used to add it.
    Displays all the recipe data and if the user changes them they get
    updated in the DB when submitted.

    Security feature to check if the user is the author of the changes are also
    learnt from my fellow student work
    https://github.com/AudreyLL88/MS3__Sante/blob/master/app.py

    """

    recipe_data = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})

    if not actual_user(recipe_data["created_by"]):
        return redirect(url_for("login"))

    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "difficulty": request.form.get("difficulty"),
            "servings": request.form.get("servings"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "recipe_image": request.form.get("recipe_image"),
            "image_source": request.form.get("image_source"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Improved!")

        return redirect(url_for("get_recipes", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Check for the user to match in order to Edit the Recipe
    if "user" in session.keys():
        user = session["user"].lower()

        if user == session["user"].lower():
            return render_template("edit_recipe.html", recipe=recipe)

        else:
            return redirect(url_for("home"))

    else:
        return redirect(url_for("login"))


# ------- Delete Recipe Page -------


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):

    """

    Allows the user to delete the recipes they created from the database

    """

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")

    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
