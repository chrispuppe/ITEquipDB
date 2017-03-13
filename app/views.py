from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app import models
from datetime import datetime, date

def string_to_date(d_string):
    new_date = datetime.strptime(d_string, '%m/%d/%Y')
    return new_date


@app.route('/' )
def index():
  post = models.Employee.query.all()
  return render_template('index.html', post=post)

@app.route('/employee/add' , methods=['POST', 'GET'])
def employee_add():
    if request.method == 'POST':
        post = models.Employee(request.form['name_form'], 
            request.form['skill_level_form'], request.form['email_address_form'], 
            request.form['trade_form'])
        db.session.add(post)
        db.session.commit()
        # db.session.refresh()
        # flash('New entry was successfully posted with ID: {0}'.format(post.id))     
 
    return render_template('employee/add.html')

@app.route('/employee/edit/<int:id>' , methods=['POST', 'GET'])
def edit_employee(id):
    #Getting user by primary key:
    # Validate url to ensure id exists
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
def delete_employee(id):
    post = models.Employee.query.get(id)
    db.session.delete(post)
    db.session.commit()
    flash ('deleted')
	   
    return redirect(url_for('index'))

@app.route('/computers' , methods=['POST', 'GET'])
def all_computers():
    post = models.Computers.query.all()
    return render_template('/computers/computers.html', post=post)


@app.route('/computers/add' , methods=['POST', 'GET'])
def computer_add():
    #raise exception
    if request.method == 'POST':
        post = models.Computers(request.form['computer_name'], request.form['brand'],
            request.form['model'], request.form['serial'],
            request.form['computer_type'], request.form['operating_system'],
            request.form['notes'], request.form['aquired_date'],
            request.form['purchase_price'], request.form['vendor_id'], 
            request.form['warranty_start'], request.form['warranty_length'], 
            request.form['warranty_end'])

        db.session.add(post)
        db.session.commit()
    return render_template('computers/add.html')

@app.route('/computers/edit/<int:computer_id>' , methods=['POST', 'GET'])
def computer_edit(computer_id):

    # Validate url to ensure id exists
    post = models.Computers.query.get(computer_id)
    if not post:
        flash('Invalid post id: {0}'.format(computer_id))
        return redirect(url_for('index'))

    # raise exception
    if request.method == 'POST':
        # raise exception
        post.computer_name = request.form.get('computer_name')
        post.brand = request.form['brand']
        post.model = request.form['model']
        post.serial = request.form['serial']
        post.computer_type = request.form['computer_type']
        post.operating_system = request.form['operating_system']
        post.notes = request.form['notes']
        post.aquired_date = string_to_date(request.form['aquired_date'])
        post.purchase_price = request.form['purchase_price']
        post.vendor_id = request.form['vendor_id']
        post.warranty_start = string_to_date(request.form['warranty_start'])
        post.warranty_length = request.form['warranty_length']
        post.warranty_end = string_to_date(request.form['warranty_end'])

        
        db.session.commit()
        return redirect(url_for('all_computers'))
    else:
        return render_template('computers/edit.html', post=post)

@app.route('/computer/delete/<computer_id>' , methods=['POST', 'GET'])
def delete_computer(computer_id):
    post = models.Computers.query.get(computer_id)
    db.session.delete(post)
    db.session.commit()
    flash ('deleted')

    return redirect(url_for('all_computers'))