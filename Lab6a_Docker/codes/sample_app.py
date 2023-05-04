# Add to this file for the sample app lab
from flask import Flask, request, render_template

sample = Flask(__name__)

#goodbye = "Good bye!"

@sample.route("/")
def main():    
    return render_template("index.html", goodbye="Good bye!")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)