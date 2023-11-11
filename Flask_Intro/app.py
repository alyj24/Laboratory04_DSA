from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/toUpperCase', methods=['GET', 'POST'])
def toUpperCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcirle', methods=['GET', 'POST'])
def areaofcircle():
    result = None
    if request.method == 'POST':
        input_radius = request.form.get('value', '')
        result = 3.14 * (float(input_radius) ** 2)
    return render_template('circular_area.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    result = None
    if request.method == 'POST':
        input_base = request.form.get('base', '')
        input_height = request.form.get('height', '')
        result = 0.5 * float(input_base) * float(input_height)
    return render_template('triangular_area.html', result=result)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
