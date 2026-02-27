from flask import Flask, url_for, request, render_template, session, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "testing_key"

# users = {
#     'user1' : {'password_hash' : 'hashed_password1'},
#     'user2' : {'password_hash' : 'hashed_password2'}
# }

users = {
    'user1': {'password_hash': generate_password_hash('1')},
    'user2': {'password_hash': generate_password_hash('2')}
}

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validate_login(username, password):
            return log_user_in(username)    
        else:
            error = "invalid creds"

    return render_template('login-form.html', error=error)
    #return f"<h1>Login Page</h1> <a href='/'>back to home | </a> <a href='/user'>to user page</a>"

def validate_login(username, password):
    user = users.get(username)
    if user:
        return check_password_hash(user['password_hash'], password)
    return False

def log_user_in(username):
    session['username'] = username
    return redirect(url_for('user'))

@app.route('/user')
def user():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f"Welcome {session['username']}"

#####################################

@app.route("/register", methods=['GET', 'POST'])
def register():
    pass

@app.route('/about')
def about():
    return "about information"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', person = name)

# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))