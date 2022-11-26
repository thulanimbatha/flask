from flask import Flask
app = Flask(__name__)
# __name__ is a special attribute - used to get the name of the current file

# this creates a basic HTML file which has all our information inside the <body></body> tag

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

if __name__ == "__main__":
    app.run(debug=True)