from flask import Flask, request, render_template
from stories import story  # Import the story instance from stories.py
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "reed"

@app.route('/home')
def home_page():
    """Returns the main page of the application."""
    return render_template('homepage.html', title='Home Page')



@app.route('/')
def ask_story():
    prompts = story.prompts  # Get the list of prompts from the story
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():

    text = story.generate(answers)
    return render_template('story.html', text=text)

