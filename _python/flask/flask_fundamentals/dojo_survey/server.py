from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def index2():
    print ('Show user info')
    print(request.form)
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    comment= request.form['message']
    gender = request.form['gender']
    spoken_languages=request.form.getlist('speak[]')
    
    return render_template("show.html", name=name,location=location,language=language,comment=comment,gender=gender,speak=spoken_languages)
if __name__ == "__main__":
    app.run(debug=True)

