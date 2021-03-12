## Testing

The testing process below inludes:

- Testing user stories
- Validating HTML, CSS, JavaScript and Python
- Checking responsiveness of design on all screen sizes
- Manually testing the functionality of all links


To return to the previous document, please click [here](https://github.com/Nicola2309/MS3/blob/master/README.md).

- [**Testing User Stories**](#Testing-User-Stories)
    - [Project Stakeholder](#Project-stakeholder)
    - [New users](#New-users)
    - [Returning Users](#Returning-Users)
    - [Frequent User](#Frequent-User)
- [**Validating the project code**](#Validating-the-project-code)
    - [HTML](#HTML)
    - [CSS](#CSS)
    - [JavaScript](#JavaScript)
    - [Python](#Python)
- [**Compatibility tests**](#Compatibility-tests)
    - [Using different browsers](#Using-different-browsers)
    - [Using different screen sizes](#Using-different-screen-sizes)
- [**Manual tests**](#Manual-tests)
    - [Navigation](#Navigation)
    - [Home](#Home)
    - [Recipes](#Recipes)
    - [Recipe](#Recipe)
    - [Articles](#Articles)
    - [Login](#Login)
    - [Register](#Register)
    - [Profile](#Profile)
    - [Edit profile](#Edit-profile)
    - [Add recipe](#Add-recipe)
    - [Edit recipe](#Edit-recipe)
- [**Bugs**](#Bugs)

### Testing user stories

#### Project stakeholder

- As the creator of this project I wanted to make sure that users would actually find value in using the website as that would be an incentive for them to return to it.
I created a project easy to navigate and to use, there is a full access to content and recipes as a guest user and, if the user is logged in they can easily add new recipes to the cookbook and personalise their page.

#### New Users

- The new user who's passionate about cooking and wants to have an online place to store and learn new recipes will find this website will be happy to have this website. They would find that it's easy to get registered and begin to add, edit and delete their own recipes.
- The student user will easily find all the recipe he might want, together with enough content to get an idea of what an healthy diet is and how to manage to organise themselves and their meals through the articles linked in the section.

#### Returning users

- This returning user wants to remember which recipe they shared some time before. They can log back in into the website, go to their profile page and check among the shared recipes which was the desired one.
-  This returning user saw a different and better way to make a recipe they previously uploaded, so they return to the website, login and decide or to search for the recipe directly in the searcbox in the recipes page or in their shared recipes section of the profile page.
- This user used the website to navigate through the articles some time ago, they forget who published the original articles but remembered that they accessed them through this cookbook. The user returns to the website and accesses the article section to read the desired article again.

#### Frequent user

- This frequent user checks often for newly added recipes or comes back often to add some new ones.

### Validating the project code

#### HTML
Ny HTML code passed through the [W3C Markup Validation Service](https://validator.w3.org/).
- Failed
    * The 4 pictures in the carousel were missing the alt property
    * `type=text` is not required in a textarea element.

There were also errors related to the creation of the HTML files through Jinja templates.
1. *Non-space characters found without seeing a doctype first. Expected <!DOCTYPE html>.*
2. *Element <head> is missing a required instance of child element 'title'.*
3. *Bad value: for attribute 'x' on element 'y' illegal character*
As each HTML base.html, the individual documents do not declare the doctype, set the language or include a head element.These errors were therefore present on each file I tested, except for base.html that fulfilled the requirements. This error was expected and did not lead to any changes.

4. *Bad value: 'url for'*
As with the first error, this was common across all HTML template files. It was also to be expected, as the validator was not anticipating to find `href="...url_for..."`


![Error: HTML file structure](https://github.com/Nicola2309/MS3/blob/master/static/images/testing/jinja-errors.png)

#### CSS
I checked my CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). 
This test passed without any errors.

#### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript code.
The test passed without any errors.

#### Python
I used [PEP8](http://pep8online.com/checkresult) to check my Python code.
I had an extra space in line 281.
![Error: Python extra space](https://github.com/Nicola2309/MS3/blob/master/static/images/testing/python-error.png)


### Compatibility tests

#### Using different browsers

I manually tested the project on the following web browsers, checking that all aspects worked as planned:
- Google Chrome 
- Mozilla Firefox 
- Ecosia
- Microsoft Edge

This did not lead to any errors or problems.

#### Using different screen sizes

I manually tested the design of the live project by doing the following:

- Using Google Developer Tools to view the project on devices with different screen sizes.
- Asking for feedback from friends and family who opened and interacted with the project on their devices.

### Manual tests

#### Navigation

When the user clicks on navigation elements the site is expected to bring the user to the corresponding website section:

- Controlling each navigation item link leading to the correct section:
    *Home - Passed. The site acted as expected
    *Recipes - Passed. The site acted as expected
    *Recipe - Passed. The site acted as expected
    *Articles - Passed. The site acted as expected
    *Login - Passed. The site acted as expected
    *Register - Passed. The site acted as expected
    *Profile - Passed. The site acted as expected
    *Edit Profile - Passed. The site acted as expected
    *Add Recipe - Passed. The site acted as expected
    *Edit Recipe - Passed. The site acted as expected
    *Responsive Device Tools using dev tools - Passed. The site acted as expected

#### Home
- *About us* button - Passed, directs the user to the expected section
- *Recipes* button - Passed, directs the user to the recipes page
- *Articles* button - Passed, directs the user to the articles page

#### Recipes
- Shows the user all the Shared recipes which the user can search through.
- *Searcbox* - Passed, when digited the name of a recipe the searchbox shows it eiter we press enter or the *Search* button.
- *Reset* / *All* button - Passed, when clicked they reload the page showing all the recipes uploaded.
- *Breakfast* - Passed, when clicked loads all the recipes with the 'Breakfast' category
- *Lunch* - Passed, when clicked loads all the recipes with the 'Lunch' category
- *Dinner* - Passed, when clicked loads all the recipes with the 'Dinner' category
- Clicking the recipe name - Passed, the user is directed to the recipe page
- *READ MORE...* button - Passed, the user is directed to the recipe page
- *Edit* button -  Passed, the user is directed to the edit recipe page
- *Delete* button - Passed, the user gets the modal question back, to ask if they really want to delete the recipe
- *Go Back* modal button - Passed, the user is directed to the recipes page
- *Delete*  modal button - Passed, the user gets the modal message back

#### Recipe
- The user see al the data from the recipe page as specified in the README file. If the user is equal to the creator of the recipe or the admin, the user can see two extra buttons.
- *Edit* button -  Passed, the user is directed to the edit recipe page
- *Delete* button - Passed, the user gets the modal question back, to ask if they really want to delete the recipe
- *Go Back* modal button - Passed, the user is directed to the recipes page
- *Delete*  modal button - Passed, the user gets the modal message back
- "Back to Recipes" button, Every user can see it - Passed, the user is directed to the recipes page

#### Articles
The user sees a card with different articles, when clicking on the titles of the articles the user is directed to their original website.
*Every article link* - Passed, the site works as expected.

#### Login
- Trying to submit the Login form with empty form values does not work as they are required fields
- Submitting the form with the incorrect combination of password and username leads to the following flash message error: 'Incorrect Username and/or Password, try again'
- With the correct username and password, a user successfully gets redirected to their 'Profile' page
- *Register* text - directs users to register page

#### Register
- Trying to submit the register form with empty form values does not work as they are required fields
- Submitting a the form with a username that is already taken leads to the following flash message error:'This username already taken, try with a new one!'

#### Profile
- *Edit* button -  Passed, the user is directed to the edit profile page
- *Delete* button - Passed, the user gets the modal question back, to ask if they really want to delete the profile
- *Go Back* modal button - Passed, the user is directed to the profile page
- *Delete*  modal button - Passed, the user gets the modal message back
- *Add Recipe* button - Passed, the user is directed to the add recipe page
* Shared recipes:
    - *READ MORE...* button - Passed, the user is directed to the recipe page
    - *Edit* button -  Passed, the user is directed to the edit recipe page
    - *Delete* button - Passed, the user gets the modal question back, to ask if they really want to delete the recipe
    - *Go Back* modal button - Passed, the user is directed to the recipes page
    - *Delete*  modal button - Passed, the user gets the modal message back

#### Edit profile
- The user gets a form in which they can change the username, email, password or user image. The inputs cannot be empty, every field is required.

#### Add Recipe
- This page is very intuitive, the user gets a form containing all the input fields to create the new recipe. All the input fields are required, so they cannot be empty.
- *Add Recipe* button - Passed, the user uploads the recipe and gets the flash message: 'Recipe Shared!'
- *Back to Recipes* button - Passed, the user is directed to the recipes page

#### Edit recipe
- This page is very intuitive, the user gets a form containing all the input fields already filled by the recipe data. All the input fields are required, so the user can change them but notleave them empty.
- *Save Changes* button - Passed, the user uploads the recipe and gets the flash message: 'Recipe Shared!'
- *Cancel* button - Passed, the user is directed to the recipes page


### Bugs

When clicking at the edges of the plus icon in the add/edit recipe page, which is used to add a new line for ingredients or procedure steps, instead of adding a new input line the user gets at the top of the page. Unsolved.

I didn't find any other interesting bug.



Return to the general README file clicking [here](https://github.com/Nicola2309/MS3/blob/master/README.md)