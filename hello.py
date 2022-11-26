from flask import Flask
import random
app = Flask(__name__)
# __name__ is a special attribute - used to get the name of the current file

# this creates a basic HTML file which has all our information inside the <body></body> tag
# app decorator
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragragh</p>' \
            '<img src="https://media.giphy.com/media/llKJGxQ1ESmac/giphy.gif">'

@app.route('/bye')
def say_bye():
    return "Bye"

# using variables, converting to a specific data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Awe {name}! You are {number} years old"

randomNumber = random.randint(0,10)
@app.route("/guess_number/<int:guess>")
def number_guess(guess):
    if guess < randomNumber:
        return '<h2>Too Low</h2>' \
            '<img src="https://media.giphy.com/media/duf84Bx74ujSXvJs0I/giphy.gif">'
    elif guess > randomNumber:
        return '<h2>Too High</h2>' \
             '<img src="https://media.giphy.com/media/vyTnNTrs3wqQ0UIvwE/giphy.gif">'
    else:
        return f'<h1>You got it, {randomNumber}</h1>' \
                '<img src="https://media.giphy.com/media/SJXKbJAoo3HXhjdV74/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)