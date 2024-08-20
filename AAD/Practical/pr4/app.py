from flask import Flask, render_template, request 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template('index.html') 

# Route for Task 1 page
@app.route('/task1')
def task1():
    return render_template('task1.html')






if __name__ == '__main__': 
    app.run(debug=True) 