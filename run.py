#export FLASK_APP=run.py
#export FLASK_ENV=development
#flask run

# So far we have:
#   1) Starting page
#   2) Questions for landlords (2 pages)
#   3) Profile view of a tenant

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

#localhost:5000/landlord
@app.route('/landlord')
def landlord():
    return render_template("landlord_first_page.html")

#localhost:5000/tenant
@app.route('/tenant/<tenant_name>')
def tenant(tenant_name):
    return render_template("tenant_profile_page.html",
        tenant_name=tenant_name)

# Keep this at the bottom of run.py
app.run(debug=True)
