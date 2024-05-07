from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawbery_count=request.form['strawberry']
    raspberry_count=request.form['raspberry']
    apple_count=request.form['apple']
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    student_id=request.form['student_id']
    
    return render_template("checkout.html",strawberry=int(strawbery_count),raspberry=int(raspberry_count),apple=int(apple_count), name1=first_name,name2=last_name,id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    