from flask import Flask
app = Flask(__name__)
# __name__ is a special attribute - used to get the name of the current file
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return "Bye"

# if __name__ == "__main__":
#     app.run()