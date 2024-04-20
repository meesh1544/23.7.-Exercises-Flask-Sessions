from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'very_secret_key'  # Needed to use sessions

@app.route('/')
def home():
    return "Go Fish Game - <a href='/start'>Start Game</a>"

if __name__ == "__main__":
    app.run(debug=True)