from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "hello world!"

@app.route('/dojo')
def dojo():
     return "dojo"

@app.route('/say/<name>')
def michael(name):
     return f"hi {name}"

@app.route('/repeat/<int:num>/<string:word>')
def hello(num,word):
     output=''

     for i in range(0,num):
          output +=word
     return output

if __name__=="__main__":
     app.run(debug=True) 