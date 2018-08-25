from flask import Flask, render_template
app = Flask (__name__)


@app.route('/')
def index ():
    return render_template('gateway.html')

@app.route('/support')
def support ():
    return render_template('support.html')

@app.route('/food')
def food ():
    return render_template('food.html')

@app.route('/shelter')
def shelter ():
    return render_template('shelter.html')

@app.route('/organizations')
def organizations ():
    return render_template('organizations.html')

@app.route('/medical')
def medical ():
    return render_template('medical.html')

@app.route('/technology')
def technology ():
    return render_template('technology.html')





if __name__ == "__main__":
    app.run(debug=True)