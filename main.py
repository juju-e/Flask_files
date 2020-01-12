from flask import Flask, render_template, request, send_file,redirect
from werkzeug import secure_filename
import sqlite3 
app = Flask(__name__)
@app.route('/')
def main():
   conn = sqlite3.connect('datas.db')
   conn.row_factory = sqlite3.Row
   cur = conn.cursor()
   cur.execute("SELECT * from files") 
   rows = cur.fetchall()
   return render_template("index.html",rows = rows)


@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      title=request.form['title']
      f.save(secure_filename(f.filename))
      conn=sqlite3.connect("datas.db")
      texts=open(f.filename).read()[:100]+"..."
      conn.execute("INSERT INTO files (name,title,body)VALUES (?,?,?)",(f.filename,title,texts))
      conn.commit()
      return redirect("/")
@app.route('/preview/<file>')
def preview(file):
  files=open(file)
  data=files.read()
  return render_template('preview.html', data=data, name=file)
@app.route('/preview/download/<file>')
def download(file):
	return send_file(file)

if __name__ == '__main__':
   app.run(port=2000,debug = True)