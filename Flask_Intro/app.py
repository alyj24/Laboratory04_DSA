from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works1():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcirle', methods=['GET', 'POST'])
def works2():
    result = None
    if request.method == 'POST':
        input_radius = request.form.get('value', '')
        result = 3.14 * (float(input_radius) ** 2)
    return render_template('circular_area.html', result=result)

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

if __name__ == "__main__":
    app.run(debug=True)
