from flask import Flask, render_template
app = Flask(__name__)
app.debug = True


#@app.route('/<name>/<age>/', methods=['GET'])
@app.route('/')
@app.route('/<name>/<age>/', methods=['GET','POST'])
def hello(name='Anonymuse', age='Unknown'):
#def hello():

    return render_template('index.html', name=name, age=age)
    #return 'Hello visitor'
    #return render_template('templates/index.html', name=name, age=age)

app.run()
