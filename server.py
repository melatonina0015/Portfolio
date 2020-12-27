from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return "form submitted"
    else:
        return "error"

