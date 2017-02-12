import os
from peewee import *
from connectdatabase import ConnectDatabase
from models import Story
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/list')
def list():
    story = Story.select().order_by(Story.id.desc)
    return render_template('list.html',story=story)

@app.route('/add', methods=['POST'])
def add_stories():
    storytitle=request.form['storytitle']
    userstory=request.form['userstory']
    criteria = request.form['criteria']
    businessvalue = request.form['businessvalue']
    estimation = request.form['estimation']
    status = request.form['status']


    new_stories = Story.create(storytitle=storytitle,userstory=userstory,criteria=criteria,businessvalue=businessvalue,estimation=estimation,status=status)
    new_stories.save()
    flash('New entry was successfully posted')
    return redirect(url_for('list'))

if __name__ == "__main__":
    app.run(debug=True)