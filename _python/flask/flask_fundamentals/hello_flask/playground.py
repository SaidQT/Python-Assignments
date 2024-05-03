from flask import Flask, render_template # type: ignore
app = Flask(__name__)    
@app.route('/play')          
def playGround():
    return render_template('index.html',var=3 , color='#9fc5f8')
@app.route('/play/<num>')
def multipleBoxes(num):
    return render_template('index.html',var=int(num),color='#9fc5f8')
@app.route('/play/<num>/<color>')
def multipleBoxesColor(num,color):
    return render_template('index.html',var=int(num),color=color )
if __name__=="__main__":     
    app.run(debug=True)    
