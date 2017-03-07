from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app import models
 
@app.route('/' )
def index():
  post = models.Employee.query.all()
  return render_template('index.html', post=post)

@app.route('/employee/add' , methods=['POST', 'GET'])
def employee_add():
    if request.method == 'POST':
        post = models.Employee(request.form['name_form'], 
            request.form['skill_level_form'],
            request.form['email_address_form'], request.form['trade_form'])
        db.session.add(post)
        db.session.commit()
        # db.session.refresh()
        # flash('New entry was successfully posted with ID: {0}'.format(post.id))     
 
    return render_template('employee/add.html')

@app.route('/employee/edit/<int:id>' , methods=['POST', 'GET'])
def edit(id):
    #Getting user by primary key:
    post = models.Employee.query.get(id)
    if not post:
        flash('Invalid post id: {0}'.format(id))
        return redirect(url_for('index'))

    # raise exception
    if request.method == 'POST':
        post.name = request.form.get('name_form')
        post.skill_level = request.form['skill_level_form']
        post.email_address = request.form['email_address_form']
        post.trade = request.form['trade_form']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('employee/edit.html', post=post)

@app.route('/employee/delete/<id>' , methods=['POST', 'GET'])
def delete(id):
     post = models.Employee.query.get(id)
     db.session.delete(post)
     db.session.commit()
     flash ('deleted')
	   
     return redirect(url_for('index'))

@app.route('/computers/add' , methods=['POST', 'GET'])
def computer_add():
    None
    # if request.method == 'POST':
    #     post = models.Employee(request.form['name_form'], 
    #         request.form['skill_level_form'],
    #         request.form['email_address_form'], request.form['trade_form'])
    #     db.session.add(post)
    #     db.session.commit()