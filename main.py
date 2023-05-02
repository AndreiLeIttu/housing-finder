from flask import Flask, render_template
from forms import FilterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7215535b018cb068bf7e26cb750baa05'

print(1)

@app.route("/")
@app.route("/home")
def home():
    form = FilterForm()
    return render_template('home.html', title='Home', form = form)