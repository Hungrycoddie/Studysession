from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['nm']
        return render_template('submit.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)