from flask import Flask , render_template , jsonify , request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate" , methods = ['GET' , 'POST'])
def generate():
    if request.method == 'POST':
        output = request.form
        return jsonify({"a" : "b"})




app.run(host = '0.0.0.0' , port=81)