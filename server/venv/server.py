# import flask to create the server
from flask import Flask

# create the app
app = Flask(__name__) 

# this is our first endpoint
@app.get("/")
def home():
    # return the
    return "hello from flask"
@app.get("/about")




# when i save code, the changes will be applied 
app.run(debug=True)



products = []

@app.get()