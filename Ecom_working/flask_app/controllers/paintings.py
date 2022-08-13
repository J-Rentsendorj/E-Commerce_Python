from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.painting import Painting

##!CREATE
## TODO Show the new model form
@app.route('/painting/new')
def new_painting():
    return render_template('new_painting.html')

@app.route('/create/painting', methods=['POST'])
def create_painting():
    print(request.form)
    painting = Painting.save(request.form) 
    return redirect("/dashboard")

##! READ
@app.route('/dashboard')
def dashboard():
    return render_template('painting.html', paintings = Painting.get_all())

@app.route('/painting/show/<int:id>')
def show_painting(id):
    data = {'id': id}
    return render_template('show_painting.html', painting = Painting.get_one(data))

#! UPDATE
## TODO route to edit painting form
@app.route('/painting/edit/<int:id>')
def edit_painting(id):
    data = {'id': id}
    painting = Painting.get_one(data)
    return render_template('edit_painting.html', painting = painting)

## TODO handle painting edit
@app.route('/painting/update', methods=['POST'])
def update_painting():
    print(request.form)
    painting = Painting.update(request.form)
    print(painting)
    return redirect('/dashboard')

@app.route('/painting/destroy/<int:id>')
def destroy(id):
    data ={
        'id' : id
    }
    Painting.destroy(data)
    return redirect('/dashboard')