from flask_app import app
from flask import render_template, redirect, request, session, flash

@app.route('/')
def enter():
    return redirect('/umbrella_man')

@app.route('/umbrella_man')
def home():
    return render_template('umbrella_man_home.html')

@app.route('/umbrella_man/about')
def about():
    return render_template('umbrella_man_about.html')

@app.route('/umbrella_man/videos')
def videos():
    return render_template('umbrella_man_videos.html')

@app.route('/umbrella_man/discography')
def discography():
    return render_template('umbrella_man_discography.html')