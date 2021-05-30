from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('cv.html')

@app.route('/resume')
def resume():
    return render_template('cv1.html')

@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')

@app.route('/contact_list')
def contactList():
    return render_template('contactList.html')

@app.route('/linkedIn')
def linkedIn():
    return redirect("https://www.linkedin.com/in/hadas-porat/")

@app.route('/hobbies')
def hobbies_page():
    return render_template('assignment8.html',
                           name="",
                           currect_user={'firstname': "Hadas", 'lastname': "Porat"},
                           hobbies=['reading', 'swimming', 'movies', 'music', 'sports'])


if __name__ == '__main__':
    app.run(debug=True)
