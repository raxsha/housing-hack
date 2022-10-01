#export FLASK_APP=run.py
#export FLASK_ENV=development
#flask run

#!/venv/bin/python
from flask import Flask, render_template

#Flask instance
app = Flask(__name__)

#router decorator
@app.route('/')

#home
#def index():
    #return '<h2>Hello tenants and landlords!</h2>'

def index():
    return render_template("index.html")

#localhost:5000/landlord/john
@app.route('/landlord/<name>')

def landlord(name):
    return '<h1>Hello {}</h1>'.format(name)
    #return db.landlord_full_name()

# Keep this at the bottom of run.py
app.run(debug=True)
