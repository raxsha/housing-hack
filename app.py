#export FLASK_APP=run.py
#export FLASK_ENV=development
#flask run

# So far we have:
#   1) Starting page
#   2) Questions for landlords (2 pages)
#   3) Profile view of a tenant

#!/venv/bin/python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename

#Flask instance
app = Flask(__name__)

# Form security - CSRF token. Usually don't push to github
WTF_CSRF_SECRET_KEY = 'a random string'
app.config['SECRET_KEY'] = "house hacking"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nhpuuxqkpekdav:5f76d1b0e5295e2fc3d75bb110ad5cf00abb1bdef48c5dc9dd0746d9e107ffeb@ec2-34-194-40-194.compute-1.amazonaws.com:5432/d7krpdvdcs52qr'

# wtforms API - https://wtforms.readthedocs.io/en/3.0.x/
# Tenant profile form class
class TenantProfileForm(FlaskForm):
    # validator to ensure data is entered
    name = StringField("What's your name?", validators=[DataRequired()])
    job = StringField("Current or previous jobs (if any)")
    family = StringField("Family members moving with you (if any)")
    pets = StringField("Pets (if any)")
    contributions = StringField("What do you want to contribute to your future neighborhood?", validators=[DataRequired()])
    volunteering = StringField("Tell us about your volunteer involvements", validators=[DataRequired()])
    bio = StringField("What else would you want your future landlord & neighbors to know about you?", validators=[DataRequired()])
    photo = FileField('Please upload a profile picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField("Submit")

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
@app.route('/tenant_michael')
def tenant_michael():
    return render_template("tenant_michael.html",
        tenant_name="Michael",
        tenant_bio="Michael received his GED in 2021 and aspires to become a high school teacher science teacher. He dreams of living in a neighborhood with a community garden that he can volunteer at. In his spare time, Michael enjoys riding his bike and playing with his puppy, Muffy.")

#localhost:5000/tenant
@app.route('/tenant_dana')
def tenant_dana():
    return render_template("tenant_dana.html",
        tenant_name="Dana",
        tenant_bio="Dana loves gardening and growing her own vegetables.")

# Create tenant's page
@app.route('/tenant_profile', methods=['GET', 'POST'])
def tenant_profile():
    name = None
    form = TenantProfileForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        filename = secure_filename(form.photo.data.filename)
    else:
        filename = None
    return render_template("tenant_profile.html",
    name=name,
    form=form,
    filename=filename)

# Keep this at the bottom of run.py
app.run(debug=True)
