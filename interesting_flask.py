
from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    #print(url_for('static',filename='favicon.ico'))
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    #print(url_for('static',filename='favicon.ico'))
    return render_template(page_name)  


def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method =='POST':
    try:
      data=request.form.to_dict()
      write_to_csv(data)
      return redirect('/thank_you.html')
    except:
        return 'did not save to database'
  else:
    return 'something went wrong'