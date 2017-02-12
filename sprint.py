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

@app.route('/story')
def story():
    return render_template('form.html')

@app.route('/')
def index():
    return redirect(url_for('list'))

@app.route('/and/list')
def list():
    stories = Story.select().order_by(Story.id.asc())
    return render_template('list.html',stories=stories)

@app.route('/delete/<id>')
def delete(id):
    row = Story.get(Story.id == id)
    row.delete_instance()
    return redirect(url_for('list'))

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