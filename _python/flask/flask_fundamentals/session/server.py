from flask import Flask, render_template, redirect ,session,request
app = Flask(__name__)   
app.secret_key='this is a secret'                
    
@app.route('/')                           
def visit_times():
    if 'visits' and 'counter' in session:
        session['visits'] += 1
        session['counter']+=1
    else:
        session['visits'] = 1
        session['counter']=1
    return render_template('index.html',visits=session['visits'],counter=session['counter'])  

@app.route('/2', methods=['POST'])
def double_visit():
    session ['visits']+=1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect ('/')

@app.route('/num',methods=['POST'] )
def add_num():
    print (request.form)
    num=request.form['quantity']
    session ['visits']+=(int(num)-1)
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)                   

