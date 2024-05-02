from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'  


@app.route('/say/<name>')
def ask_name(name):
    return "Hi "+name

@app.route('/repeat/<int:num>/<name>')
def print_name(name, num):
   return '<br>'.join([name] * num)

if __name__=="__main__":     
    app.run(debug=True)    


