from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app import models
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, date
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash


# validation and str to date for input
def string_to_date(d_string):
    try: 
        new_date = datetime.strptime(d_string, '%m/%d/%Y')
    except:
        new_date = datetime.now().date()
    return new_date


# grabs a new employee list from DB
def fresh_employee_list():
    choose_employee = models.Employee.query.all()
    # Sort employees by name
    choose_employee.sort(key=lambda x: x.name, reverse=False)
    return choose_employee

##############################################################################
# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('all_employees'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = models.User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

###############################################################################
@app.route('/employee' )
@login_required
def all_employees():
    post = fresh_employee_list()
    return render_template('employee/employees.html', post=post)


@app.route('/employee/add' , methods=['POST', 'GET'])
def employee_add():
    if request.method == 'POST':
        post = models.Employee(
            request.form['name_form'], request.form['skill_level_form'], 
            request.form['email_address_form'], request.form['trade_form']
            )
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
    employees = models.Employee.query.all()
    return render_template('/computers/computers.html', employees=employees, post=post)


@app.route('/computers/add' , methods=['POST', 'GET'])
def computer_add():

    employee_list = fresh_employee_list()
    # raise exception
    if request.method == 'POST':
        post = models.Computers(
            request.form['computer_name'], request.form['brand'],
            request.form['model'], request.form['serial'],
            request.form['computer_type'], request.form['operating_system'],
            request.form['notes'], 
            string_to_date(request.form['aquired_date']),
            request.form['purchase_price'], request.form['vendor_id'], 
            request.form['warranty_length'], request.form['assigned_to']
            )

        db.session.add(post)
        db.session.commit()
    return render_template('computers/add.html', employee_list=employee_list)


@app.route('/computers/edit/<int:id>' , methods=['POST', 'GET'])
def computer_edit(id):
    # new employee list for form
    employee_list = fresh_employee_list()

    # Validate url to ensure id exists
    post = models.Computers.query.get(id)
    if not post:
        flash('Invalid post id: {0}'.format(id))
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
        
        post.warranty_length = request.form['warranty_length']
        

        
        db.session.commit()
        return redirect(url_for('all_computers'))
    else:
        return render_template('computers/edit.html',employee_list=employee_list,
                post=post)


@app.route('/computer/delete/<id>' , methods=['POST', 'GET'])
def delete_computer(id):
    post = models.Computers.query.get(id)
    db.session.delete(post)
    db.session.commit()
    flash ('deleted')

    return redirect(url_for('all_computers'))