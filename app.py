from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # This would normally handle form submission with database or email
        # For demo purposes, we'll just redirect back to the contact page
        return redirect(url_for('contact', submitted=True))
    
    submitted = request.args.get('submitted', False)
    return render_template('contact.html', active_page='contact', submitted=submitted)

if __name__ == '__main__':
    app.run(debug=True) 