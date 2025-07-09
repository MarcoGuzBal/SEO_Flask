from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name
proxied = FlaskBehindProxy(app)
app.config["SECRET_KEY"] = '8b9e08405c4d567642f74e5e84df7aee'

@app.route("/")
def home():
  return render_template('home.html', subtitle='Home Page', text='This is the home page')

# @app.route("/second_page")
# def second_page():
#   return render_template("second_page.html", subtitle='Second Page', text="This is the second page")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
