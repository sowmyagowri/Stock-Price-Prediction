from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

""""
@app.route('/predict/<companyname>', methods = ['POST'])
def prediciton():
	comp = request.form['companyname']
	return "The company selected is %s" % companyname
"""

@app.route("/")
def prediction():
	return render_template("index_272.html")

@app.route('/result' , methods = ['POST', 'GET'] )
def result():
	if request.method == 'POST':
		companyname = request.form['companyname']
		#companyname = float(request.form['companyname'])
		companyname = companyname + 5
		#return "The company selected is %s" %companyname	
		return render_template("result.html", compname = companyname)



if __name__ == "__main__":
	app.run(debug=True)