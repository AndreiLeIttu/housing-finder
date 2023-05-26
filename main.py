from flask import Flask, render_template, url_for, redirect
from forms import FilterForm
from apartments_getter import get_from_pararius

app = Flask(__name__)

app.config['SECRET_KEY'] = '7215535b018cb068bf7e26cb750baa05'

filters = {
    "city" : "",
    "minPrice" : "",
    "maxPrice" : "",
    "rooms" : "",
    "interior" : "",
    "size" : ""
}   

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = FilterForm()
    if form.validate_on_submit(): 
        global filters
        filters["city"]=form.city.data
        filters["maxPrice"]=form.max_price.data
        filters["minPrice"]=form.min_price.data
        filters["rooms"]=form.rooms.data
        filters["interior"]=form.interiorType.data
        filters["size"]=form.size.data
        return redirect(url_for('list'))
    else:
        print(2)
    return render_template('home.html', title='Home', form = form)

@app.route("/list")
def list():
    links = get_from_pararius(filters)
    print(links)
    return render_template('apartments_listing.html', title='List')