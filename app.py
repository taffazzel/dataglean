from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Add your email sending logic here
        return redirect(url_for('thank_you'))
    return render_template('contact.html', form=form)

@app.route('/thank_you')
def thank_you():
    return "Thank you for your message!"

if __name__ == '__main__':
    app.run(debug=True)