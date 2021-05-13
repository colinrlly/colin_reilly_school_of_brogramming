# Assignment 12
Hello

## Objective
The big obj: Let's sauce up this front end application with some JavaScript (very different from Java).

The front end of an application is broken into 3 different languages which each accomplish a different function...
1. HTML takes care of the *structure* of the client. This is used to define what the front-end *is* - what buttons, text fields, paragraphs, etc are on the page.
2. CSS takes care of the *sytle* of the client. This is used to define how the front-end *looks* - colors, spacing, margins, fonts, etc. In today's age CSS is much more powerful then it used to be, often handling things like transitions.
3. JavaScript takes care of the *functionality* of the client. This is used to define what the front-end *does* - what happens when you click the button, making API calls to the back end, etc.

HTML is markup language, CSS is a stylesheet language, and JavaScript nowadays is a full fledged object oriented, functional, scripting language. JavaScript has a weird past but today it is a full blown language used all over the stack (front end and back end).

## Instructions
1. Currently our applications have a text field which we type our query into using our keyboard. This isn't how a calculator works at all!!! A calculator uses buttons to add to the text field. So, let's create all the buttons we need to make the calculator work. Currently we are not going to focus on style so when we do this assignment our calculator is going to look like a big stack of buttons on top of each other, we'll style it later. I like to get the structure and functionality completely done before I style anything I write. That way I can focus on making sure the application functions 100% without being bogged down by moving buttons around and whatnot. Guess this line number was just explanation :).
2. First we need to do some django configuration to get static files to work in our app (static files are css, javascript, images). Add `import os` to the top of your `settings.py` file. Then add the following code below the `AUTH_PASSWORD_VALIDATORS` block.
```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
This tells Django where to find your static files.
3. Let's create a bunch of buttons in our template. In HTML a button looks like this `<button type='button'>+</button>`. Inside your form create the buttons you will need on your calculator (+, -, /, *, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, C, backspace). I'll leave it up to you what the complete set of buttons will be. If we dont say `type='button'` in our button it will submit the form when clicked.
4. Now, let's add some JAVASCRIPT.
5. Create a file in the `<django_app>/static/js` directory called `calculator.js`. In my application this goes under `chad_django/chad_django/static/js`.
6. Then in your html file add this line as the first line `{% load static %}` then to include the javascript script in your page add below that `<script src="{% static 'js/calculator.js' %}"></script>`
7. Now in your `calculator.js` file create a function called `add_to_input` which takes the argument `to_add`. (JavaScript has different syntax then Python so you'll need to look up how to define a function).
8. This new JavaScript function should add the argument to the end of the input text field. Look into `document.querySelector` in order to select the text input element. Here's some sudo code to help you figure out how to do this.
```
select the text input element on your page
append to the value of the text input element
```
9. Now that we have a function which can append onto the end of our input all we need to do is make our buttons call this function when they are clicked! So for each button on your page add the `onclick` attribute and in that onclick value call our new function `add_to_input` with the argument set to the thing we want to append to the input (add_to_input('+') for the plus button etc.).
10. At this point whenever you click a button it should append to the end of your input and work just like a normal calculator. Then you just click calculate like normal and it will send the query to your backend like normal.
11. You might also want to add a clear button to clear the input. 

## Resources
* [Write a minimal form](https://docs.djangoproject.com/en/3.1/intro/tutorial04/#write-a-minimal-form)

Tabs that I have open on my comp after figuring this all out:
* [Separation of business logic and data access in django](https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django)

## Due Date
4/7/21 7PM MST
