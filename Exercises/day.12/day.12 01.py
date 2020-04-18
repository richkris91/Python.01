from flask import Flask, render_template
app = Flask(__name__)
app.debug = True


@app.route('/name/<name>/<age>/')
def hello(name, age):
    return render_template('index.html', name=name, age=age)


app.run()
