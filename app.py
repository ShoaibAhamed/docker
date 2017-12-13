from flask import Flask,jsonify
import json


app = Flask(__name__)
jData = json.loads(open('./emp.json').read())
data=jData["Employee"]

@app.route('/')
def Emp_main():
    return "RESTful API Assignment"

@app.route('/getemp/')
def emp_all():
    mList=[]
    for element in data:
        mList.append(element)
    return jsonify(mList)

@app.route('/getemp/<string:id>/')
def emp_id(id=''):
    mList=[]
    for element in data:
        if element['id'] == id:
            mList.append(element)
    result = jsonify(mList)
    return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
