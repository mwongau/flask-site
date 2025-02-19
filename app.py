from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/photos")
def photos():
    return render_template('photos.html') 
    
@app.route("/privacy")
def privacy():
    return render_template('privacy.html') 
 
@app.route("/blog")
def blog():
    # for testing in local PC, DATABASE = 'db.sqlite'
    # When it is hosted in PythonAnywhere, DATABASE= 'flask-site/db.sqlite'
    # Change the database name db.sqlite to your own database name
    DATABASE = 'db.sqlite' # setting for testing in local PC
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    rows = con.execute("select * from tb1 order by id desc").fetchall()
    con.close()
    return render_template("blog.html", rows=rows)    
    
if __name__=="__main__":
    app.run()
 