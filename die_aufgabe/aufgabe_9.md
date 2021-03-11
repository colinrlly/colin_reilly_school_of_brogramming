# Assignment 9

## Objective
1. Consolodate the two apps. I had you create a new app with the `manage.py startapp` command, but I have since decided that is not the best method. Manually merge your sub-app code in with the app folder that is named the same as your root project folder. You will need to make a views.py file in the master app folder to do this.
2. Download Postman. An API creation tool which will allow you to create mock POST/GET etc. calls to your server.
3. Create a new Postman request which POSTs to the url `localhost:8000/api/calculate`.
4. Go to the Body tab beneath the url bar and select raw from the radio buttons. This will allow you to input JSON data which will be sent to the backend along with your POST request.
5. Input the following into the raw field in the Body tag:
```
{
    "to_calculate": "4+5",
}
```
6. Click the big `Send` button in the top right. You should recieve some sort of failing information in the `Response` section of Postman. This is expected as you have not created the endpoint in your Django server to handle the incoming request.
7. In your Django app create a new endpoint in your urls file to handle the incomming request. The new endpoint should be `api/calculate/`. Create a new view/function in your `view.py` file called `calculate` and point the newly created url to it.
8. Program the view function to accept `JSON` `POST` data which will come in the Django `requests` object. Print the JSON to your console using the familiar `print(xxx)` function. After this is completed you will have accepted your first api request from an external source. The request coming from Postman is not so different than the request that comes from Chrome when you type localhost:8000 into the browser. Chrome makes a `GET` `HTTP` request where we will be making a `POST` `HTTP` request. The two types of requests are similar but the GET request puts its query information in the url like this: `localhost:8000?im_a_query=parameter`, and the POST request puts it's query information hidden away in the POST data. When the Django server recieves a GET request from Chrome it usually returns some `HTML` code and this is how web pages are rendered. In our current case we want the Django server to return `JSON` when we recieve the POST request from Postman. JSON is a convenient standard data format that is easily convertible to and from a string. It is also a very human readable data format that makes it great to work with.
9. Return some JSON to Postman by following this [Stackoverflow](https://stackoverflow.com/questions/9262278/how-do-i-return-json-without-using-a-template-in-django) post. 
10. Now when you make your POST request from Postman you should see in the Response section the JSON object you returned from your Django view.


## Resources
* [Stackoverflow post on returning JSON from Django view](https://stackoverflow.com/questions/9262278/how-do-i-return-json-without-using-a-template-in-django)
* [Postman](https://www.postman.com/)
* [Postman learning center](https://learning.postman.com/)
* [JSON webpage](https://www.json.org/json-en.html)
* [Django views documentation](https://docs.djangoproject.com/en/3.1/topics/http/views/)
* [W3schools article on GET vs POST requests](https://www.w3schools.com/tags/ref_httpmethods.asp)

## DUE DATE
3/10/21 7pm bthurorbsqr
