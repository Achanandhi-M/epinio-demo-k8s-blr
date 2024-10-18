from pymongo import MongoClient
import os
from flask import Flask, redirect, url_for, render_template, request

uri = os.environ.get('MONGODB_URI')
app=Flask(__name__,static_url_path='/static',static_folder='static')

# Create a new client and connect to the server
client = MongoClient(uri)

def create_user_data(name,email,password,rePassword):
    client = MongoClient(uri)

    try:
        database = client["user-db"]
        collection = database["user-table"]
        user_data = {
        "name" : name,
        "email" : email,
        "password": password,
        "re-password":rePassword,
}
        result = collection.insert_one(user_data)

    except Exception as e:
        raise Exception("Error inserting the value: ", e)

    client.close()

@app.route('/',methods=['POST','GET'])
def input():
    if request.method=='POST':
        name=request.form['username']
        email=request.form['email']
        password=request.form['password']
        rePassword=request.form['re-password']

        if name and email and password and rePassword:
            create_user_data(name,email,password,rePassword)
            return redirect(url_for('output'))
        else:
            return "please fill out all fields"
    return render_template('index.html')


@app.route('/output',methods=['GET'])
def output():
    return render_template('response.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)