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
@app.route('/list',methods=['GET'])
def list():
    stories = Story.select().order_by(Story.id.asc())
    return render_template('list.html',stories=stories)

@app.route('/story/<id>', methods=['GET','POST'])
def story(id):
    if Story.select().where(Story.id == id).exists():
        user_story = Story.get(Story.id == id)
    else:
        user_story=None
    return render_template("form.html",user_story=user_story)

@app.route('/delete/<id>')
def delete(id):
    row = Story.get(Story.id == id)
    row.delete_instance()
    return redirect(url_for('list'))


@app.route('/add', methods=['GET','POST'])
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


@app.route('/update_story', methods=['POST'])
def update_story():
    id=request.form['id']
    storytitle=request.form['storytitle']
    userstory=request.form['userstory']
    criteria = request.form['criteria']
    businessvalue = request.form['businessvalue']
    estimation = request.form['estimation']
    status = request.form['status']
    user_story = Story.update(storytitle=storytitle,
                              userstory=userstory,
                              criteria=criteria,
                              businessvalue=businessvalue,
                              estimation=estimation,
                              status=status).where(Story.id == id)
    user_story.execute()
    return redirect(url_for('list'))

if __name__ == "__main__":
    app.run(debug=True)