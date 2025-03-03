from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Add your email sending logic here
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "Thank you for your message!"

if __name__ == '__main__':
    app.run(debug=True)