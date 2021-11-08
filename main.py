from flask import Flask, render_template, request,redirect, url_for
from new import names, Last_name, Address, City
from fuzzywuzzy import fuzz

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    duplicate = False 
    if request.method == 'POST':
        form = request.form 
        duplicate = ddupe(form)

    return render_template('uttp.html', duplicate = duplicate) 

def ddupe(form):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    city = request.form['city']
    first_name_ratio = fuzz.token_set_ratio(first_name, names)
    last_name_ratio = fuzz.token_set_ratio(last_name, Last_name)
    address_ratio = fuzz.token_set_ratio(address, Address)
    city_ratio = fuzz.token_set_ratio(city, City) 

    similarity_ratio = ((first_name_ratio + last_name_ratio + address_ratio + city_ratio)/400)
    
    if similarity_ratio > 0.55:
        duplicate = "potential duplicate"
    else:
        duplicate = "good to go" 

    return(similarity_ratio, duplicate)


if __name__ == "__main__":
  app.run(debug=True)