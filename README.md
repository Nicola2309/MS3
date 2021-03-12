# SustainEat

## Code Institute: Milestone Project 3

![SustainEat Responsive Design](https://github.com/Nicola2309/MS3/blob/master/static/images/wireframes/responsive-pic.png)

*SustainEat* is an online cookbook that helps people focus on the importance of a balanced diet. My aim with this project was to create an intuitive website, useful for people which want to eat better, and enjoyable for everyone.

I changed many diets in my life often decided by the time I had to prepare my food, I always searched for the perfect one that could give me all the nutrients needed to have a balanced performance throughout the days of the week and that wouldn't stress my body due to some nutrients missing.
Beside the guidelines of the World Health Organization I am happy I came across the [Harvard Summary of Studies](https://www.hsph.harvard.edu/nutritionsource/sustainability/plate-and-planet/#planetary-health-diet) on beneficial dietary patterns to adopt, resulting in a healthier therefore more energetic life.

[Here the full project live.](https://eat-sustainable-project.herokuapp.com/)

## Table of contents

- [**UX**](#UX)
    - [Main aims](#Main-aims)
    - [User Stories](#User-Stories)
        - [Project Stakeholder](#Project-Stakeholder)
        - [New Users](#New-Users)
        - [Returning Users](#Returning-Users)
        - [Frequent User](#Frequent-User)
    - [Design Process](#Design-Process)
- [**Features**](#Features)
    - [Database structure](#Database-structure)
    - [Existing features](#Existing-features)
    - [Features left to implement](#Features-left-to-implement)
- [**Technologies used**](#Technologies-used)
- [**Testing**](https://github.com/Nicola2309/MS3/blob/master/testing.md)
- [**Deployment**](#Deployment)
    - [Local deployment](#Local-Deployment)
    - [Deploying this project to Heroku](#Deploying-this-project-to-Heroku)
- [**Credits**](#Credits)
    - [Content](#Content)
    - [Images](#Images)
    - [Acknowledgements](#Acknowledgements)

## UX

### Main aims

- To create a website with real-world value for users searching for better diet ideas

- Allow the user to Create, Update or Delete their own recipes and Read all the recipes created by other users

- To make the navigation intuitive through a fixed navbar and clear buttons throughout the webpages and create a design fully responsive on all device screen sizes

### User Stories

The following User Stories helped me to create a design that would satisfy the needs of several different types of users.

#### Project Stakeholder

- I am the creator of the website and I want to see it succeed. I would like to attract users searching for quality based recipes and see them return to find and share simple and healthy ideas for a meal.

#### New Users

- I am a user who loves cooking and follows many cooking channels on the web, I would like to find an online cookbook where I can store and find new recipes.
- I am a student user who needs to eat healthy to stay fit and focused, I would like a website in which I can find all the recipes I need to have an idea of a correct diet.

#### Returning Users

- I am a user who uploaded a nice recipe some months ago but I forgot which one was it, I want to Log in my profile to check which recipes I have already shared.
- I am a user who found a better version of the recipe I previously uploaded, I want to modify according to the new version I saw.
- I am a user who used the website to read practical articles on shopping and preservation of food, I come back to the website to use the links and access the articles.

#### Frequent User

- As a frequent user, I want to come back to the website and search or add new recipes. 

### Design Process

#### Design Process: UX Research

Prior to decide which design to develop I searched for other food blogs already on the internet to check their design and structure to import or change in mine.
My research helped understand that:
- I wanted to create an online cookbook surrounded by inspiring content that would encourage the user to upload specific kinds of recipes.
- I needed simple steps to add a recipe and to find it in the website through a database search box and some buttons to have only the desired category of recipes displayed.

#### These are the website visited in the research process:
- [Budget Bytes](https://www.budgetbytes.com/)
- [Cooking Classy](https://www.cookingclassy.com/)
- [Downshiftology](https://downshiftology.com/)
- [Pich of Yum](https://pinchofyum.com/)
- [The Recipe Critic](https://therecipecritic.com/)


#### Design process: UX Design

1. Strategy plane: While searching for other blogs I saw that there wasn't one designed around the latest studies on the best diet for a human body, and the planet. My goal became make a website for the user interested in eating better without having to buy expensive products and bring the latest dietary studies in a easy-to-use, and engaging website.

2. Scope plane: With the app idea and the goal in mind I started to consider the functionalities of the website. Adding the CRUD functions to allow the user to engage with the website a personalised relationship, creating their profile, welcoming them by their username and upload recipes beside consulting them.

3. Structure plane: Once decided which feature would have been part of my project I started to consider its structure.
I wanted to divide the content according to the state of the user.
If the user is a guest user without a profile would be allowed to navigate through the 'Home', 'Recipes', 'Articles', 'Login' and 'Register' page.
If the user is registered and has a profile will be able to navigate to its 'Profile' page and will have the ability to upload recipes through the 'Add Recipe' page.

4. Skeleton plane: With a structure concept clear I began to think of the user navigation through the design.
In the landing page the user would see immediately two buttons, one to keep reading the Homepage and the website mission and the other to jump the the 'Recipes' page to meet the needs of a new and curious user and a returning one.
When the user decides to Register or Login they will have access to their profile page with a default picture if the link chosen is broken, and they will be able to see a section 'Shared Recipes' that will show the recipes shared by the user if shared, and when more than 6 there will be a pagination to go through all the recipes shared.
Adding a recipe for the logged user will be with a simple form and a 'plus' icon to add every ingredient of the recipe and every step of its preparation.

5. Surface plane: The main stylistic decision was to keep the design with bright light colors through the website, mainly shades of green and orange. The website that helped me managing the colour shades and palettes was [Mycolor Space](https://mycolor.space/), as shown below. I wanted to create a sense of joy and relax with green and of creativity with orange.

I went then on Google Fonts to find two compatible fonts that would recall a grandma cookbook writing for titles and found the Lily Script One, and a steady font for the website content, and i chose the Montserrat for this purpose.
I then decided to use the Lily Script One only for the navbar, not to overload the website with style and keep it simpler.


### Documenting the design process

Selected color palettes:
![Shades palette from Mycolor Space](https://github.com/Nicola2309/MS3/blob/master/static/images/wireframes/shades-palette.png)

![Squash palette from Mycolor Space](https://github.com/Nicola2309/MS3/blob/master/static/images/wireframes/squash-palette.png)

Design on desktop devices:
![Design for desktop](https://github.com/Nicola2309/MS3/blob/master/static/images/wireframes/wireframe-desktop.png)

Design on tablet devices:
![Design for tablets](https://github.com/Nicola2309/MS3/blob/master/static/images/wireframes/wireframe-tablet.png)

Design on mobile devices:
![Design for mobile](https://github.com/Nicola2309/MS3/blob/master/static/images/wireframes/wireframe-mobile.png)

The entire workspace can be views with this [link](https://www.figma.com/file/jc8QKDwQCQ1ecvrTFuogfB/MS's?node-id=0%3A1)

## Features

### Existing Features

This project consists of ten pages, four of which can be accessed only when the user is logged in.

#### Database structure

The data of this project are stored in my MongoDB database within three collections:
- *Categories* - This collection stores the different categories of the recipes, whether they are intended for 'Breakfast', 'Lunch' or 'Dinner'
- *Recipes* - When a user uploads a recipe the data is sent to this collection with the following information: The recipe name, the category, the preparation time, the difficulty, a brief description, an array with its ingredients, the preparation steps and finally the recipe picture, the credits for the image and the user profile who created the recipe.
- *Users* - This collection stores the user's username, encrypted password, email and user profile picture.

#### Consistent features across all pages

- The navbar is visible and responsive in every page, and when the user scrolls down it turns into white and follows the navigation.
- All the 'Add Recipe' and 'Go Back' / 'Cancel' buttons areof the same color throughout the design, the only exception is the one in the user profile, but it gets the typical green color when hovered.
- All the flash messages appear with the same color and font throughout the app.

#### Imagery
The landing picture has a big red pepper falling into water communicating freshness to the user, blending with the side text following the design rule of having 3 objects in proportion. In this case the big pepper, the medium sized side text and buttons and the smaller navigation links.

#### Homepage

- The user reads two short sentences tha explain immediately what the website purpose is, make them prepare healthy days.
- The user has two options, or continuing the reading of the content or jump to the recipes page.
- Scrolling down, the user reads the idea behind the website in 3 brief paragraphs.
- Proceeding further the user can see the ["Healthy Eating Plate"](https://github.com/Nicola2309/MS3/blob/master/static/images/harvard-plate.jpg), the use is kindly permitted from Harvard with the mandatory rule of adding the copyright under the picture in the website and that it wouldn't be associated to any commercial purpose website.
There the user will find a button that brings them to the Articles page.
- The third and last section is dedicated to cooking together and being a team in the kitchen so to ease the work for everyone and prepare more things, a carousel with five different pictures suggests all the situations in which people can team up and prepare food.

#### Recipes

- This page offers the user a different approach to the view of the recipes, they can decide to search the recipes by name or by clicking one of the four buttons to get displayed only recipes of a specific category.
- If the user is logged and corresponds to the creator of one of the displayed recipes they will have the possibility to see the 'Edit' and 'Delete' buttons, the admin can always see the buttons.

#### Single recipe

- This page shows the user the recipe image in a card, and next to the user can see the category, the preparation time, the difficlulty, the number of servings and the username who created the recipe. Under the pictures the Credits from the picture are clearly readable
- Beneath this section the user can read the Brief Description of the recipe, the Ingredients List and the Procedure steps.

#### Articles

- This page offers the articles to the user with related pictures and a brief explanation of what they will find in the article.

#### Login

- The existing user is welcomed with a 'Welcome back, ()', with the parenthesis containing the username of the logged user.
- If any of the combinations between username and passwords are wrong the user gets a flash message suggesting that one of the two inputs or both are wrong.
It is not specified which one is wrong as a security feature to protect the accounts from malitious users.
- If the user doesn't have an account it is prompted to register through a clickable 'Register' word next to the Login button.

#### Register

- New users are welcomed with a 'Welcome, Food Lover!' flash message after registering through a simple form ascking for their username, email, password and profile picture.
- If the user has an account it is prompted to login through a clickable 'Login' word next to the Register button.

#### Profile

- When the user logged in or is registered they are redirected to the 'Profile' page where they can see their profile picture and the section with the button to add a new recipe and beneath that section another displaying the recipes shared by the user, if any, and a pagination if the number of shared  recipes is greater than 6.

#### Edit Profile

- This page gives the possibility to the user to change their username, email, password or profile picture to restyle their profile.
- There are two different buttons at the bottom of the page, one to save the changes and  one to cancel the changes and get redirected to the profile page.

#### Add recipe

- This page lets the logged in user add a new recipe in the cookbook. The user is asked to fill a form with all the recipe data like the name, category, preparation time, difficulty, recipe image, credits of the image, a brief description, the ingredients and the preparation steps.

#### Edit recipe 

- If the user created a recipe or is the admin, the user can decide to Edit or Delete that recipe. In the Edit page the user gets all the current data from the recipe and can decide to add or change ingredients or any other input the user decides to change.
- Under the Edit form the user have the options to save the changes or cancel the actions through two buttons.

### Features Left to implement

- There is still a lot of potential implementations to further develop in this website. Most notably, I would consider adding the total cost of a single recipe based on price indicators per ingredient, but is beyond the scope and time frame of this Milestone Project with *The Code Institute*.

- Would be nice to introduce a rating system for every recipe to see the most popular ones.

- I would also consider a common page with all the users profiles that can show their Weekly Meal Plan to the other users by filling a form.

## Technologies Used

### Languages, libraries, databases, frameworks, editors and version control

- [HTML5](https://html.com/)

- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)

- [Javascript](https://www.javascript.com/)

- [jQuery](https://jquery.com/)

- [Python](https://www.python.org/)

- [Pymongo](https://pymongo.readthedocs.io/en/stable/)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

- [MongoDB](https://www.mongodb.com/)

- [Materialize](https://materializecss.com/)

- [Gitpod](https://www.gitpod.io/)

- [Git Version Control](https://git-scm.com/)

- [GitHub](https://github.com/)

- [Heroku](https://www.heroku.com/)

### Additional tools

- [Figma](https://www.figma.com/) 
    * Figma helped me design my project, by creating wireframes for desktop, tablet and mobile devices. 
- [FontAwesome](https://fontawesome.com/) 
    * I relied on free FontAwesome icons for this project.
- [Canva](https://www.canva.com/)
    * I used canva to create the website Logo.
- [Google Fonts](https://fonts.google.com/)
    * I used two complementary fonts from Google for my project.
- [Pexels](https://www.pexels.com/)
    * This website was one of the sources for the images contained throughout the project.
- [Pixabay](https://pixabay.com/)
    * This website was another one of the sources for the images contained throughout the project.
- [Am I Responsive](http://ami.responsivedesign.is/)
    * This website was used to implement the responsive image of my website in the project. 
- [Microsoft Phots](https://www.microsoft.com/en-us/p/microsoft-photos/9wzdncrfjbh4?activetab=pivot:overviewtab)
    * This simple tool helped me shrink the pictures to share on the Readme file.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    * This was a great tool throughout the project to check whether there were any errors in my HTML code (as discussed in more detail in the Testing section).
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    * This was a great tool throughout the project to check whether there were any errors in my CSS code (as discussed in more detail in the Testing section).
 - [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code (explained in more detail in the Testing section). 
- [PEP 8 online](http://pep8online.com/)
    * I used PEP 8 to check that my Python code complied with formatting standards. 

## Testing

Please view the complete testing process in [this separate document](https://github.com/Nicola2309/MS3/blob/master/testing.md).

## Deployment

This project was developed using Gitpod as the chosen IDE and Github as a remote repository.

The deployed project can be viewed on the following link: [SustainEat: Live Website](https://eat-sustainable-project.herokuapp.com/)

The project's GitHub repository can be viewed with the following link: [SustainEat: Github Repository](https://github.com/Nicola2309/MS3)

### Local deployment

If you would like to work on this project further you can clone it to your local machine using the following steps:

1. Scroll to the top of this repository and click on the "clone or download button"
2. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    * HTTPS: click on the checklist icon to the right of the URL to copy it
    * SSH key: first click on 'Use SSH' then click on the same icon as above
3. Open a new Terminal window in your IDE of choice
4. Change the current working directory to the location where you want the cloned directory.
5. Enter the following command and press 'Enter' to create your local clone:
```
git clone https://github.com/Nicola2309/MS3.git
```

6. Now create a Database that you intend to use for this cloned project with MongoDB.
7. Return to the Terminal and enter the following to install all required dependencies:
```
pip3 install -r requirements.txt
```
8. Create an env.py file with the following content, replacing the 'username','password', 'cluster_name' and 'database_name' with your MongoDB database values:
```
import os

os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" 
```
9. Add your env.py file to .gitignore to make sure your database information is not viewable to others
10. Your cloned version is now ready to run locally with the following command:
```
python3 app.py
```

You can find both the source of this information and learn more about the process with the following link: [Cloning a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Deploying this project to Heroku

1. I created a Heroku account, signed in and created a new app with a unique name that had not already been taken (this project uses 'eat-sustainable-project'). I then set the region to the closest to me: 'Europe'.
2. With the app created, I went to the 'Settings' tab and clicked the 'Reveal Config Variables' button. From here, I input the following values:
```
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
IP: 0.0.0.0
PORT: 5000
```
(Note: within the MONGO_URI value, I replaced the 'username','password', 'cluster_name' and 'database_name' with my specific database values. They are kept private for security reasons.)


3. In Gitpod, I created a requirements.txt file with the following command:
```
pip3 freeze --local > requirements.txt
```
4. I then created a Procfile with the following content within (making sure that 'Procfile' was written with a capitalized 'P'):
```
echo web: python app.py > Procfile
```
5. I then committed these new files with the following:
```
git add .
```
```
git commit -m ""
```
6. With these files committed, I logged in to Heroku using this command and entered my details at the prompt:
```
heroku login
```
7. Once logged in, I linked my Heroku app created above as the remote repository with this command:
```
heroku git:remote -a ms3-move-on
```
8. I then completed the deployment by pushing the projekt to Heroku:
```
git push heroku master
``` 
9. This completed the process of deploying the project to Heroku. Once deployed, I continued to push all changes made to the project to Heroku throughout the remaining development process.

## Credits

### Content

Website Text: Beside the copyright text for the [Harvard Plate](https://github.com/Nicola2309/MS3/blob/master/static/images/harvard-plate.jpg) and the Articles title in the Articles html page, all the text in the website was written by myself.

### Images

The Images from Pexels and Pixabay are referenced below

#### Pexels

- [Kid hand holding a plant](https://www.pexels.com/photo/person-holding-a-green-plant-1072824/)

- [Plate of chicken and salad](https://www.pexels.com/nl-nl/foto/gekookt-eten-1860208/)

- [Two bowls of Ramen](https://www.pexels.com/nl-nl/foto/groentesalade-3026808/)

- [Mother and daughter preparing food](https://www.pexels.com/nl-nl/foto/moeder-en-dochter-die-avocadotoost-voorbereiden-4259707/)

- [Girl eating cookies and grandma talking](https://www.pexels.com/nl-nl/foto/nadenkend-grootmoeder-met-kleindochter-met-interessant-gesprek-tijdens-het-samen-koken-in-lichte-moderne-keuken-3768146/)

- [Kid mixing pasta supervised by two adults](https://www.pexels.com/nl-nl/foto/mannen-met-een-kind-in-een-keuken-4261782/)

- [Family around a mom cooking](https://www.pexels.com/nl-nl/foto/foto-van-vrouw-koken-in-de-buurt-van-haar-familie-3807332/)

- [A person making dough](https://www.pexels.com/nl-nl/foto/persoon-met-wit-poeder-op-bruin-houten-tafel-6287264/)

- [Open fridge containing vegetables]( https://www.pexels.com/nl-nl/foto/voedsel-gezond-groenten-apple-4443442/)

- [Plate filled with cut vegetables on a table with vegetables and spices on](https://www.pexels.com/nl-nl/foto/plat-lag-fotografie-van-groentesalade-op-plaat-1640777/)

- [View of crop fields and hills](https://www.pexels.com/nl-nl/foto/bruine-en-groene-bergzichtfoto-842711/)

#### Pixabay

- [Paprika in water](https://pixabay.com/nl/photos/paprika-water-fruit-rood-voedsel-5126804/)

- [Couple preparing food](https://pixabay.com/nl/photos/vrouw-keuken-man-dagelijks-leven-1979272/)

- [Planet earth on a plant](https://pixabay.com/nl/illustrations/aarde-globe-geboorte-nieuwe-405096/)

- [Planet earth in a light bulb](https://pixabay.com/nl/photos/aarde-planet-continenten-licht-2581631/)

- [Weekly timetable](https://pixabay.com/nl/illustrations/tijdschema-papier-print-template-3224768/)

## Additional support

I used this tutorials and code pieces to add different functionalities to the website.

- [Changing navbar color after scrolling](https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling)

- Stick the footer at the bottom when the page is emptier from [smashtheshell](https://www.youtube.com/watchv=TaXql0h_wCA&ab_channel=smashtheshell)

- Code inspired from my fellow student [iainm342](https://github.com/iainm342/milestone-3/blob/main/static/js/recipe.js) to add extra ingredients and preparation steps lines in the 'Add Recipe' form, through Javascript.

## Acknowledgements

- My mentor [Seun Owonikoko](https://github.com/seunkoko) for her attention to detail throughout the development process
- The talented *Code Institute* tutors for the advices, guidance and support
- And as always, a big thank you to [Miranda Thewlis](https://github.com/mkthewlis) and her inspiring and well made repositories and documentation
-  Thanks to my family and friends as well for giving me honest feedback throughout