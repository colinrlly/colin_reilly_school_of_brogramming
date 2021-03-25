# Assignment 12

## Objective
Set up a template to render some HTML.

1. Create a templates folder under to django app - mine is `chad_django/templates`.
2. Put an html file in the new templates folder. The html path should be `<YOUR_APP>/templates/index.html`.
3. Inside that newly created html file put some html code: `<p>Hello World!<p>`.
4. In your `views.py` file import the render method at the top of your file by putting in `from django.shortcuts import render`.
5. Render the html file in your index view by typing `return render(request, 'index.html')` - this should be the only code in your index view.
6. Django will automatically look for the `index.html` file in your templates directory (this is a Django convention). Start your server and go to whichever url renders your index view by typing the url in your browser. You should see `Hello World!` in your browser.

`pog` We will now create a form to hit our calculate endpoint.

7. In your `index.html` file type:
```
<h1>Calculate something</h1>

<form action='/calculate' method='get'>
    {% csrf_token %}
    <label for='calculator_input'></label>
    <input type='text' name='calculator_input'/>
    <input type='submit' value='calculate' />
</form>
```
8. This `html` file is going to look very new and there is a lot of stuff going on in here. First, anything wrapped in `{% %}` is not actually html but is instead part of the Django templating language. The Django templating language allows us to pass information from our views into the html file easily. Other then that syntax this is perfectly normal html. Forms are a complicated topic and are built into html. I won't go too deep into how the html file is structured but the main takeaway is that when the submit button is clicked the page will be redirected to the `/calculate` endpoint along with the `GET parameters to_calculate=<YOUR_INPUT>`. All together that means our server will recieve a request like this `/calculate?to_calculate=<YOUR_INPUT>`.
9. Additionally here is what my `urls.py` file looks like now. I will just show it because I had to do some tricky configuration to get it to work. Of course my two views are named `index` and `calculate` and yours might be different. Don't copy this verbatim but instead use it to troubleshoot your urls file.
```
urlpatterns = [
    path('', views.index, name='index'),
    path('calculate', views.calculate, name='calculate'),
    path('admin/', admin.site.urls),
]
```
10. Now, instead of our calculate view (or whatever yours is called) accpeting JSON from Postman it is going to be accepting `GET parameters`. We will access the GET parameters in our view similar to how we tried to access POST parameters in the beginning: `request.GET.get(['calculator_input'], None)`. Switch out the JSON parsing / grabbing logic in your calculate view for logic which gets the calculator input from the GET parameters. Then use whatever you get from the GET parameters as the input to your calculator class.
11. Make sure to handle the user not inputing anything and clicking submit on the front end. In other words it is possible for the result of our `.get` to return `NONE`, in this case don't run your calculator and instead return an empty response.

`pog` We are now going to do some fancy cleaning of our views and combine the calculate and index views. Notice how in your program when the user clicks submit they get redirected to another page, and if they want to do another calculation they have to click the back button to go back to the homepage. This isn't the cleanest way our calculator could work and isn't how a calculator actually works in the real world. When you click `=` in a real calculator it just shows you the answer right there. Let's combine our `index` and `calculate` views so that the user always stays on the same page. We will acomplish this by the same `if calculator_input is None don't run the calculate function` logic.

12. Before we go and mess up our views let's add a bit of logic to our html and index view. In Django you can pass a dictionary to the render method and then access the contents of that dictionary in the template. In our index view pass the dictionary `{'result': '7'}` as the third argument to the render function.
13. Now, in the html file (also called the template) add this line `<p>result: {{ result }}</p>` below the form. When you go to the index page in your browser you should now see `result: 7` on your screen.
14. Now, here comes the hard part. I will write sudo code for how your index view should work and you will need to actually implement it. After you do this step you should have only one view (`index`) which will handle both rendering the calculator form and accepting/doing the calculation. So, program your index view to do the following logic:
```
# Get the calculator_input from the get parameters with the fallback to None if it doesn't exist
# If calculator_input is truthy (not None)
    # Run the calculation
    # Save the calculation and it's result to the database
    # Render the index.html template and pass in {'result': <YOUR_RESULT>} as the third parameter.
# Otherwise if calculator_input is falsy (None)
    # Render the index.html template and don't pass in anything as the third parameter
```
15. Delete the unused `/calculate` (or equivalent in your project) url from the `urls.py` file.
16. Use your fancy new calculator UI!

## Resources
* [Write a minimal form](https://docs.djangoproject.com/en/3.1/intro/tutorial04/#write-a-minimal-form)
* [Write views that actually do something](https://docs.djangoproject.com/en/3.1/intro/tutorial03/#write-views-that-actually-do-something)
* [Django forms](https://docs.djangoproject.com/en/3.1/topics/forms/)

Tabs that I have open on my comp after figuring this all out:
* [Separation of business logic and data access in django](https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django)
* [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
* [Django design philosophies](https://docs.djangoproject.com/en/dev/misc/design-philosophies/)
* [Django can't find my templates](https://stackoverflow.com/questions/4065045/django-cant-find-my-templates)
* [HTML form method attribute](https://www.w3schools.com/tags/att_form_method.asp)
* [django MultiValueDictKeyError error, how do I deal with it](https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it)

## Due Date
3/24/21 7PM MST
