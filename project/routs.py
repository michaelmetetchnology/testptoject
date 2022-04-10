import json,time
from flask import render_template, url_for, flash, redirect,request
from project.model import User
from project.forms import RegisterationForm,LoginForm
from project import app,db


@app.route("/")
def home():
    data_set={'page':'Home','Message':'Successfly loaded the Home Page', 'Timestamp':time.time()}
    json_dump= json.dumps(data_set)
    return json_dump

@app.route("/about")
def about():
    user_query= str(request.args.get('user')) #/user/?user=FIAHVSISDAH 
    data_set={'page':'Request','Message':f'Successfly get the requist for {user_query}', 'Timestamp':time.time()}
    json_dump= json.dumps(data_set)
    return json_dump    

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterationForm() 
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account has been createted!','success')
        return redirect(url_for('login'))
    return render_template('regsiter.html',title='Register',form=form)
@app.route('/login')
def login():
    form=LoginForm() 
    return render_template('login.html',title='Login',form=form)