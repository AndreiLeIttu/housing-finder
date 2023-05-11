from flask import Flask, render_template, url_for, redirect
from forms import FilterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7215535b018cb068bf7e26cb750baa05'

print(1)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = FilterForm()
    if form.validate_on_submit(): 
        print(1)
        return redirect(url_for('list'))
    else:
        print(2)
    return render_template('home.html', title='Home', form = form)

@app.route("/list")
def list():
    return render_template('apartments_listing.html', title='List')