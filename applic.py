from flask import Flask
app=Flask(__name__)
@app.route("/")
def hom_page():
    return "Hello world"

app.route("/about")
def home_page():
    return "this is the about page"
