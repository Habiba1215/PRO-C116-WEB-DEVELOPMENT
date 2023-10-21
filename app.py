# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/index")
def home():

    name = "Habiba Hasan" # write your name
    age = "16 years" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Atharul Hasan Syed" 
    age = "45 years"

    return render_template('father.html', name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Salma Husain"
    age = "40 years"

    return render_template('mother.html', name = name, age=age )

# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "Sana Afreen , Riya Shah ,  Sobana Murugan , Ustat Sahi"
    age = "Birla Public School, Doha-Qatar"
    return render_template('friend.html', name = name,age=age )

# add other routes, if you want

# run the file
app.run()
