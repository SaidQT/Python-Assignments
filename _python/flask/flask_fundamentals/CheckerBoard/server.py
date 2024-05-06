from flask import Flask, render_template # type: ignore
app = Flask(__name__)  
@app.route('/')  
def checkboard():
    return render_template('index.html',var=8,num=8,color1='#ffffff',color2='#000000')
@app.route('/<x>')          
def checkerboard2(x):
    return render_template('index.html',var=int(x) , num=8,color1='#ffffff',color2='#000000')
@app.route('/<x>/<y>')
def checkerboard3(x,y):
    return render_template('index.html',var=int(x),num=int(y),color1='#ffffff',color2='#000000')
@app.route('/<x>/<y>/<color1>/<color2>')
def checkerboard4(x,y,color1,color2):
    return render_template('index.html',var=int(y) , num=int(x),color1=color1,color2=color2)
if __name__=="__main__":     
    app.run(debug=True)    
