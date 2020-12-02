from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
myage = 14

class get_name(FlaskForm):
	name = StringField("Please enter your name")
	age = StringField("Please enter your age")
	submit = SubmitField("Submit")

@app.route('/', methods=["GET", "POST"])
def main():
	get_nm = get_name()
	name = get_nm.name.data
	age = get_nm.age.data
	return render_template("mess.html",name_form=get_nm)

@app.route('/you/<name>/<int:newage>')
def name(name, newage):
	if myage > newage:
        theage = 'I am' + (myage - newage) + 'years older than you'
    elif myage < newage:
    	theage = 'I am ' + (newage - myage) +'years younger than you'
    return f'<h1>Hi {name.title()}</h1><br/><p>{theage}</p>'

if __name__ == "__main__":
	app.run(debug=True)
