from flask import Flask, render_template, redirect ,session
app = Flask(__name__)   
app.secret_key='this is a secret'                
    
@app.route('/')                           
def visit_times():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html',visits=session['visits'])  



if __name__=="__main__":
    app.run(debug=True)                   

